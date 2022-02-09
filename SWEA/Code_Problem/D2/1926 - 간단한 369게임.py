# 입력
N = int(input())

# 박수 치는 숫자들의 모음
claps_num = '369'

# 1부터 N+1까지
for num in range(1, N+1):
    # 박수치는 횟수 초기화
    clap = 0
    # num을 문자열화 시키고 각 자릿수의 수가 clap에 포함되면 clap 1증가
    for n in str(num):
        if n in claps_num:
            clap +=1
    # clap이 없으면 숫자 그대로 출력
    if clap == 0:
        print(num, end=' ')
    # clap이 있으면 clap한 횟수만큼 -출력
    else:
        print('-'*clap, end=' ')
