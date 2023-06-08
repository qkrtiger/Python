# 기본 출력
print(1)
print(2)
print(3)
print("abc")

a = 1; b = 2; c = 3
print(a, b, c)
print(a, b, c, sep="\t")

print('a' 'b' 'c') #아래와 같음.
print('a' + 'b' + 'c')
s1 = 'a'; s2 = 'b'; s3 = 'c'
# print(s1 s2 s3) # 오류!
print(s1 + s2 + s3)
print(s1, s2, s3, sep=", ")

end_value = '-aaa-'
print(s1, end=end_value)
print(s2, end=end_value)
print(s3)