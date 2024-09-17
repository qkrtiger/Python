def nth_multiple(x, y): # (6, 3)
    if x % y != 0:
        raise Exception(str(x) + '는/은 ' + str(y) + '의 배수가 아닙니다.')
    print(f'{x}는/은 {y}의 배수입니다.')
    
a, b = map(int, input('두 수 입력 : ').split())

try:
    nth_multiple(a, b)
except Exception as e:
    print(e)