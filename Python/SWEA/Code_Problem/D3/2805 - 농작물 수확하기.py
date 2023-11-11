for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(abs(N // 2 - i), N - abs(N // 2 - i)):
            total += arr[i][j]

    print(f'#{tc} {total}')
