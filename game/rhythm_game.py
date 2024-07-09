import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('4키 리듬게임')

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 노트 설정
note_width = 50
note_height = 50
note_speed = 10  # 속도 증가
note_frequency = 20  # 노트 생성 확률 (1~100)

# 키 설정
keys = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]
key_colors = [RED, GREEN, BLUE, YELLOW]
key_positions = [150, 300, 450, 600]

# 점수
score = 0
missed_notes = 0

# 폰트 설정
font = pygame.font.Font(None, 36)

# 노트 클래스
class Note:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, note_width, note_height)
        self.color = color

    def move(self):
        self.rect.y += note_speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# 노트 리스트
notes = []

# 시간 설정
clock = pygame.time.Clock()

# 기준선 위치
line_y = screen_height - 100

# 게임 루프
running = True
while running:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 노트 생성
    if random.randint(1, 100) <= note_frequency:
        lane = random.randint(0, 3)
        note = Note(key_positions[lane], 0, key_colors[lane])
        notes.append(note)

    # 노트 이동 및 그리기
    for note in notes[:]:
        note.move()
        note.draw()
        if note.rect.y > screen_height:
            notes.remove(note)
            missed_notes += 1

    # 기준선 그리기
    pygame.draw.line(screen, WHITE, (0, line_y), (screen_width, line_y), 5)

    # 키 입력 처리
    keys_pressed = pygame.key.get_pressed()
    for i, key in enumerate(keys):
        if keys_pressed[key]:
            for note in notes[:]:
                if note.rect.colliderect(pygame.Rect(key_positions[i], line_y - note_height // 2, note_width, note_height)):
                    notes.remove(note)
                    score += 1
                    break

    # 점수 및 놓친 노트 개수 표시
    score_text = font.render(f'Score: {score}', True, WHITE)
    missed_text = font.render(f'Missed: {missed_notes}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 50))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
