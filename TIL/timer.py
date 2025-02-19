# 함수 실행시간 출력해주는 데코레이터 함수

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        # 실행 시간 계산
        elapsed_time = end_time - start_time
        
        # 시간, 분, 초로 변환
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"{func.__name__} 실행 시간: {int(hours)}시간 {int(minutes)}분 {seconds:.2f}초")
        return result
    return wrapper

# timer 함수 사용
@timer
def sample(self):
  print('Hello')
  time.sleep(5)
