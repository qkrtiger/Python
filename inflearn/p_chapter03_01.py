# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method) 둘 다 사용
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심(파이썬 데이터모델) -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 매직 메소드 : 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(int)
# <class 'int'>
print(float)
# <class 'float'>

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))
print()
print()

n = 10

# 사용
print(n + 100)
print(n.__add__(100))
# n+100과 n.__add__(100)은 같은 결과를 출력한다.

# print(n.__doc__) -> 도움말 출력
print(n.__bool__(), bool(n)) # 0이면 False, 1이상이면 True # 같은 결과를 출력함
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    # 생성자 메소드이므로 초기화를 해준다.
    def __init__(self, name, price):
        # 인스턴스 변수 초기화
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._price >= x._price:
            return True
        else:
            return False

    # 대소비교
    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._price <= x._price:
            return True
        else:
            return False
        
    # 내가 원하는 더하기 연산을 정의할 수 있다.
    # (x+x)*0.8 
    def __add__(self, x):
        return (self._price + x._price) * 0.8

    # 뺄셈 메소드
    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._price - x._price

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1+s2)

# 일반적인 계산
# print(s1._price + s2._price)

# 매직메소드 출력
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)


## 인스턴스 변수의 특징
# 인스턴스에 종속적: 인스턴스 변수는 클래스의 인스턴스마다 고유합니다. 즉, 같은 클래스에서 생성된 각 객체는 서로 다른 인스턴스 변수를 가질 수 있습니다.
# 초기화: 인스턴스 변수는 주로 __init__ 메서드 내에서 초기화됩니다. __init__ 메서드는 객체가 생성될 때 자동으로 호출되어 인스턴스 변수를 설정합니다.
# 접근 방법: 인스턴스 변수는 self 키워드를 통해 접근합니다. self는 인스턴스 자신을 가리키는 참조 변수입니다.

# 인스턴스 사용 예제
class Dog:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수 name
        self.age = age    # 인스턴스 변수 age
    
    def speak(self):
        print(f"{self.name} says woof!")

# 두 개의 인스턴스를 생성
dog1 = Dog("Buddy", 3)
dog2 = Dog("Molly", 5)

# 인스턴스 변수에 접근
print(dog1.name)  # 출력: Buddy
print(dog2.age)   # 출력: 5

# 인스턴스 메서드 호출
dog1.speak()      # 출력: Buddy says woof!
dog2.speak()      # 출력: Molly says woof!
