a = [10, 20, 30]
print(a)
try:
    idx, x = map(int, input("순번과 나눌 숫자 입력 : ").split())
    y = a[idx] / x
    print(f'{a[idx]} / {x} = {y}')
except ZeroDivisionError as ze:
    print('0으로 나눌 수 없습니다.', ze)
except IndexError as ie:
    print(f'0부터 {len(a) - 1}까지만 순번을 입력하세요.', ie)
    
# 다른 코드들...

try:
    l = int(input('숫자 : '))
    m = 10 / l
except:
    print('0으로 나눌 수 없습니다.')
else:
    print(f'결과 : {m}')
finally:
    print('처리가 완료되었습니다.')