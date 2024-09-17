t1 = (1, 2, 3, 4)
print(t1)
print(t1[2])
#t1[1] = 10     -- 안됨
#t1.pop()       -- 안됨
#t1.insert(2,7) -- 안됨

t2 = ('a',)
print(t2)

t3 = tuple(range(10))
print(t3)

l1 = list(range(1,10,2))
t4 = tuple(l1) # 데이터의 고정화.
print(t4)

print(len(t4))

a = t4.index(9) #5의 순번(인덱스)
print(a)

# 원소의 존재 유무 확인 in/not in
# 결과는 bool 형 - True/False
b = 8 in t4
print(b)

c = 8 not in t4
print(c)

str = 'hello python world'
d = 'a' in str
e = 'a' not in str
print(d, e)