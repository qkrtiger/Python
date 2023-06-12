
a = 100 # 전역변수
def func1():
    global a # 전역변수로 지정
    a = 10 # 지역변수
    print(f'함수 안 : {a}')
    
func1()
print(f'함수 밖 : {a}')