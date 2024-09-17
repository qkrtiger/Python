# 간단한 덧셈기
#a = input('첫번째 숫자 : ')
a = int(input('첫번째 숫자 : '))
#b = input('두번째 숫자 : ')
b = int(input('두번째 숫자 : '))
#a = int(a)
#b = int(b)
c = a + b
print("결과 : " + str(c))

x, y = input("두 값를 입력 : ").split(',')
print(x)
print(y)

l, m, n = map(int, input('세 숫자를 입력 : ').split())
print(l + m + n)