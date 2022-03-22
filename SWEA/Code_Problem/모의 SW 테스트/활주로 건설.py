def canbuild(x):
    global cnt
    check = [[0] * N for _ in range(N)]

    for i in range(N):
        flag = 0
        height = sorted(list(set(x[i])))
        for idx in range(1, len(height)):
            if height[idx] - height[idx - 1] != 1:
                flag = 1
                break

        if flag == 0:
            for j in range(1, N):
                if abs(x[i][j - 1] - x[i][j]) <= 1:
                    if x[i][j] > x[i][j - 1]:
                        if 0 <= j - X < N and check[i][j - X:j] == [0] * X and len(set(x[i][j - X:j])) == 1:
                            check[i][j - X:j] = [1] * X
                        else:
                            flag = 1
                            break

                    elif x[i][j] < x[i][j - 1]:
                        if 0 <= j + X <= N and check[i][j:j + X] == [0] * X and len(set(x[i][j:j + X])) == 1:
                            check[i][j:j + X] = [1] * X
                        else:
                            flag = 1
                            break

                else:
                    flag = 1
                    break

        if flag == 0:
            cnt += 1


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    canbuild(arr)

    arr = list(zip(*arr))

    canbuild(arr)

    print(f'#{tc} {cnt}')
