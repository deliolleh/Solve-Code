# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 입력 받은 수
    given = int(input())
    # 총합 계산
    total = 0

    # 1 ~ given까지
    for j in range(1, given+1):
        # 홀수는 더하고
        if j % 2:
            total += j
        # 짝수는 빼고
        else:
            total -= j

    print(f'#{i+1} {total}')
