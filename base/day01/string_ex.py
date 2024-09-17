s1 = 'hello world~'
s2 = "hello world~"
s3 = '''hello world~'''
s4 = """hello world~"""

s5 = 'hello "python" world~'
s6 = "hello 'python' world~"

s7 = '''hello
python
world
'''
print(s7)

# 문자열 연산
# '+' : 문자열 결합
str1 = "hello"
str2 = " world"
print(str1 + str2)
# '*' : 문자열 반복
print(str1 * 3)
print("=" * 20)
print(str1[1])
print(str2[-1]) # 시퀀스의 뒤에서 부터 순번 처리