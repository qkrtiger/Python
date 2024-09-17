# 변수
base = 2

# 함수
def square(n):
    return base ** n

# 클래스
class InfoClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def show(self):
        print(f'{self.a}, {self.b}')