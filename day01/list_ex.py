l1 = [0, 1, 2, '3', 4]
print(l1)

print(l1[2])

# 원소 변경
l1[3] = 3
print(l1)

l2 = list(range(10,0,-1))
print(l2)

# 리스트 추가 삭제
# append - 리스트의 마지막에 원소 추가
l3 = []
l3.append(1)
l3.append(2)
print(l3)
# insert - 리스트의 지정 위치에 원소 삽입
l3.insert(1, 5)
print(l3)
# pop - 리스트의 마지막 원소 꺼내기(삭제)
x = l3.pop()
print(x, l3, sep='\n')
l3.append(3)
l3.append(4)
l3.append(5)
print(len(l3)) # 리스트의 크기(원소의 개수) len()
print(l3)
#y = l3.pop(2) # 순번 지정하여 원하는 위치의 값 꺼내오기
#print(y, l3, sep="\n")
#print(l3.pop())
#print(l3)
# remove - 리스트의 지정 값을 원소 삭제(첫번째 값만 삭제)
l3.remove(5)
print(l3)
# 기타 함수
# sort - 원소 정렬
l4 = [4, 5, 1, 3, 7, 2]
l4.sort()
print(l4)
l5 = ['a', 'z', 'm', 'c']
l5.sort()
print(l5)
l6 = ['가', '라', '다', '나']
l6.sort()
print(l6)
# reverse - 원소 배치 반전
l4.reverse()
print(l4)
# index - 원소의 위치값 구하기
i = l4.index(5)
print(i)

# 슬라이스(부분 추출 또는 변경)
print(l4[0:3], l4)
s1 = l4[1:4]
print(s1)
# 리스트[start:end] : start부터 end-1까지 추출.
# 리스트[start:end:step] : start부터 end-1까지 
#                       step 간격으로 추출
l4.append(0)
print(l4, len(l4))
s1 = l4[0:-1:2]
print(s1)
s1 = l4[0:len(l4):2]
print(s1)
s1 = l4[:len(l4):2]
print(s1)
s1 = l4[0::2]
print(s1)
s1 = l4[::2]
print(s1)
s1 = l4[:] # 리스트 복사(전체 추출)

l7 = list(range(0,100,10))
print(l7)

l7[2:5] = [333, 444, 555]
print(l7)

# 복원
l7 = list(range(0,100,10))
l7[2:5] = [333, 444, 555, 666, 777]
print(l7)

# 복원
l7 = list(range(0,100,10))
l7[2:10:2] = [333, 444, 555, 666]
print(l7)