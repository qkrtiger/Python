d1 = {1:'one', 2:'two'}
print(d1)
print(d1[1])
print(d1[2])

# 딕션너리에 추가
d1[3] = 'three'
print(d1)

d1['four'] = 4
print(d1)

person1 = {"name":"홍길동"}
person1["age"] = 20
person1["addr"] = "인천시 미추홀구"
print(person1)
print(person1["addr"])
# key 목록만 추출
kl = list(person1.keys())
print(kl)
# value 목록만 추출
vl = list(person1.values())
print(vl)

item = list(person1.items())
print(item)

# 값을 꺼내오는 함수 : get()
# 존재하지 않는 key를 가져올 경우
print(person1.get("phone")) # None 출력
#print(person1["phone"]) -- 오류 발생

# in을 사용하여 key 존재 유무 확인
b = "phone" in person1
print(b)