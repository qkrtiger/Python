scores = list(map(int, input("점수입력 : ").split()))

print(scores)

def sum_scores(*ss): # ss 대신 args(arguments의 약자) 용어를 주로 사용
    sum = 0
    for s in ss:
        sum += s
    return sum

sum_res = sum_scores(*scores)
print(f'총정 : {sum_res}')