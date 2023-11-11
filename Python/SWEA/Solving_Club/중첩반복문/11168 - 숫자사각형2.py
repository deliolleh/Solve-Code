# 테스트 케이스 수
T = int(input())

for i in range(1, T+1):
    x, y = map(int, input().split())

    cnt = 1
    print(f'#{i}')

    for j in range(x):
        one = []
        for k in range(y):
            one.append(cnt+k*x)
        print(*one)
        cnt += 1
