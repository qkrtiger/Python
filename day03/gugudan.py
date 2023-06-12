# 구구단 프로그램

# 단수를 입력받아서 해당 단을 출력
def multi(d):
    for i in range(1, 10):
        # print('{}*{} = {:2}'.format(d,i,d*i))
        print(f'{d} * {i} = {d*i:2d}')
        
dan = int(input('단을 입력하세요 : '))
multi(dan)