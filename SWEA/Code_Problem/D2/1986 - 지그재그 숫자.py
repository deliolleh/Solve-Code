# 테스트 케이스 수
t = int(input())

for i in range(t):
    given = int(input())
    total = 0

    for j in range(1, given+1):
        if j % 2:
            total += j
        else:
            total -= j

    print(f'#{i+1} {total}')
