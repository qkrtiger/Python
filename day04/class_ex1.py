# 클래스 정의(선언)
class info:
    def show_info(self, a):
        print('hi~', a)
    def add(self, a, b):
        print(f'{a} + {b} = {a + b:2d}')
        
# 클래스 사용(인스턴스 생성)
data1 = info()

data1.show_info('wellcome')
data1.add(10, 5)

###############################
class PersonInfo:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def show_info(self):
        print('이름 :', self.name)
        print('나이 :', self.age)
        print('주소 :', self.address)

person1 = PersonInfo('홍길동', 20, '인천시')
person1.show_info()

# 빈 클래스로 시작하여 속성을 추가
class ProdInfo:
    pass

prod1 = ProdInfo()
prod1.name = 'TV'
prod1.price = 1000000

print(prod1.name, prod1.price)

prod2 = ProdInfo()
#print(prod2.name)

# 메소드에서 속성 생성
class ProdInfo2:
    def start(self):
        self.va = 'hi!!!'
        
p1 = ProdInfo2()
p1.start() # 메소드로 속성을 만들 경우 
           # 반드시 메소드를 먼저 실행해야 함.
print(p1.va)

# 정해진 속성 외에 추가 금지. __slots__
class PersonInfo2:
    __slots__ = ["name", "age"]
    
person2 = PersonInfo2()
person2.name = "전우치"
person2.age = 30
#person2.address = "서울시" #- 새 속성(변수) 추가 금지

class ProdInfo3:
    def __init__(self, name, price, amount):
        self.name = name
        self.__price = price
        self.amount = amount
    
    def discount(self, price):
        self.__price -= price
    
    def show_info(self):
        print(self.name)
        print(self.__price)
        print(self.amount)
        
book = ProdInfo3('파이썬', 50000, 10)
print(book.name)
#print(book.__price)
print(book.amount)
book.discount(5000)
book.show_info()