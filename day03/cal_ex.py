def cal(a, b, op):
    c = 0
    if op == '+':
        c = a + b
    elif op == '-':
        c = a - b
    elif op == '*':
        c = a * b
    elif op == '/':
        c = a / b
    return c

def cal2(a, b, op):
    match op:
        case '+':
            c = a+b
        case '-':
            c = a-b
        case '*':
            c = a*b
        case '/':
            c = a/b
        case _:
            print('연산 기호를 잘못입력했습니다.')
            c = 0
    return c

x, oper, y = input('계산식 입력 : ').split()

x = int(x)
y = int(y)

res = cal2(x, y, oper)
print("계산결과 : ", res)