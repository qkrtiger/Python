#키워드 인수 방식
def person_info(name, age, addr):
    print(f'이름 : {name}')
    print(f'나이 : {age -1}') #만 나이 출력
    print(f'주소 : {addr}')
    
person_info(name='홍길동', addr='인천시', age=20)
print()
person_dic = {'name':'전우치', 'age':25, 'addr':'서울시'}
person_info(**person_dic)

def per_info(**kwargs): # 'keyword arguments'의 약자
    for kw, arg in kwargs.items(): # 딕셔너리 키와 값 쌍을 하나씩 가져옴.
        if kw == 'age':
            arg -= 1
        print(f'{kw} : {arg}')

dic1 = {'name':'고길동', 'age':45, 'addr':'서울시', 'phone':'010-1234-5678'}

per_info(**person_dic)
per_info(**dic1)