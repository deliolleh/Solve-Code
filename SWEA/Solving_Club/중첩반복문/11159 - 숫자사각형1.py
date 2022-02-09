# 테스트 케이스 수
T = int(input())

for i in range(1, T+1):
    x, y = map(int, input().split())

    cnt = 1

    print(f'#{i}')
    for i in range(x):
        one = []
        for j in range(y):
            one.append(cnt)
            cnt += 1
        print(*one)

