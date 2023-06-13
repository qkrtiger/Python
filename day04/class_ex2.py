class Box:
    entry = [] # 모든 인스턴스 공통
    
    def __init__(self):
        self.e = [] # 인스턴스별로 다름
    
    def put_entry(self, item):
        self.entry.append(item)
        
b1 = Box()
b1.put_entry('책')
b1.e.append('게임기')
b1.e.append('가방')

b2 = Box()
b2.put_entry('옷')
b2.e.append('열쇠')

print(f'b1 : {b1.entry}')
print(f'b2 : {b2.entry}')
print(f'b1.e : {b1.e}')
print(f'b2.e : {b2.e}')

class AdminMember:
    # doc string
    '''관리자용 클래스입니다.'''
    __pass = '1234'    
    
    def get_pass(self):
        '''비밀번호 지정'''
        print(AdminMember.__pass)
    def set_pass(self, ps):
        AdminMember.__pass = ps
    

admin = AdminMember()
#print(admin.__pass) -> 오류
admin.set_pass('3456')
admin.get_pass()

# doc string 활용
print(AdminMember.__doc__)
print(AdminMember.get_pass.__doc__)
print(admin.get_pass.__doc__)
