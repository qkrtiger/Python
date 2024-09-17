s1 = {1, 2, 3, 4, 5}
print(s1)

s2 = set([1, 2, 3, 4])
print(s2)

s3 = set('hello')
print(s3)

#print(s3[0]) -- 오류 -> 리스트로 변환하여 사용
l1 = list(s3)
print(l1[0])

s2.add(5)
print(s2)
s2.update([6, 7, 8, 9])
print(s2)
s2.remove(5)
print(s2)

print(8 in s2)
print(5 not in s2)

s4 = {1, 2, 3, 4, 5, 6}
s5 = {4, 5, 6, 7, 8, 9}

s6 = s4 & s5 # 교집합
print(s4, s5)
print(s6)

s7 = s4 | s5 # 합집합
print(s7)

s8 = s5 - s4 # 차집합
print(s8)