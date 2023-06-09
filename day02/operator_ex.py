x = 5
y = 2

print("x =", x, ", y =", y)
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)
print("x // y =", x // y)
print("x ** y =", x ** y)

# 출력 형식 지정(printf과 유사)
# %d - 정수, %f - 실수, %s - 문자열
# d, f, s 앞에 숫자를 넣을 경우 출력 자리개수 지정.
print("%d + %d = %2d" %(x, y, x + y))
print("x = {0}, y = {1}".format(x, y))
# {0:3} -> 첫번째 값은 3자리로 출력.
# {}로만 작성해도 작성 순서에 따라 값 대입.
# 순서 번호는 0번부터 시작.

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print(a == b)
print(a is b)
print(a is not b)

c = a
print(a == c)
print(a is c)
print(a is not c)