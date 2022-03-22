dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_catch = 0

    for i in range(N):
        for j in range(N):
            catch_t = catch_x = arr[i][j]
            for m in range(1, M):
                for k in range(8):
                    if 0 <= j + m * dx[k] < N and 0 <= i + m * dy[k] < N:
                        catch = arr[i + m * dy[k]][j + m * dx[k]]
                        if k % 2 == 0:
                            catch_t += catch
                        else:
                            catch_x += catch

            if max(catch_t, catch_x) > max_catch:
                max_catch = max(catch_t, catch_x)

    print(f'#{tc} {max_catch}')
