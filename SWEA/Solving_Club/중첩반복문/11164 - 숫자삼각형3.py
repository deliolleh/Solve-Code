# 테스트 케이스 수
T = int(input())

for i in range(1, T+1):
    x, y = map(int, input().split())

    cnt = 1

    print(f'#{i}')
    for j in range(x):
        one = [] * y
        if j % 2 == 0:
            for k in range(y):
                one.append(cnt)
                cnt += 1
        else:
            for k in range(y):
                one.append(cnt)
                cnt += 1
            one.reverse()
        print(*one)

