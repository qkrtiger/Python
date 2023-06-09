score = int(input('점수 = '))

# 조건부 표현식(삼항연산자와 유사한 방식)
# m = (score >= 60) ? '합격' : '불합격';
m = '합격입니다.' if score >= 60 else '불합격입니다.'
print(m)

# if score >= 60:
#     print('합격입니다~~')
#     print('여유를 즐기세요~')
# else:
#     print('불합격입니다!')
#     print('공부하세요!')
    
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')