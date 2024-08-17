# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화 
# 2.변수 할당 가능 -> 클로저, 코루틴으로 연결 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능

# 함수 객체
def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1) # 재귀

class A:
    pass

print(factorial(6))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A)))) # set : 중복 제거
print(factorial.__name__) # 함수 이름
print(factorial.__code__) # 함수 코드 객체

print()
print()

# 변수 할당
var_func = factorial
# var_func = factorial 함수 자체를 변수에 할당

print(var_func)
print(var_func(10))
print(map(var_func, range(1,11))) # map : 함수와 반복 가능한 자료형을 입력으로 받아 각 요소가 함수에 의해 수행된 결과를 묶어서 돌려주는 함수
print(list(map(var_func, range(1,6)))) # list로 변환


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce 등
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
# filter() 함수는 주어진 이터러블(여기서는 range(1, 6))의 각 요소에 대해 조건을 평가하여 True인 요소들만을 걸러낸다.
print([var_func(i) for i in range(1,6) if i % 2])

print()
print()

# reduce()
from functools import reduce
from operator import add

print(reduce(add, range(1,11))) # 누적
print(sum(range(1,11)))


# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 사용(익명 함수 대신)
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x + t, range(1,11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))

from inspect import signature

sg = signature(var_func)

print(sg)
print(sg.parameters)

print()
print()

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))