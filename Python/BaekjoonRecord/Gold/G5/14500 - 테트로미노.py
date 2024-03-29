dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def check_four(y, x, cnt, value):
    global max_sum, visited
    if cnt == 4:
        if value > max_sum:
            max_sum = value
    else:
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = 1
                check_four(ny, nx, cnt + 1, value + arr[ny][nx])
                visited[ny][nx] = 0


def check_three(y, x):
    global max_sum
    for t in range(4):
        sum_three = arr[y][x]
        for d in range(t, t + 3):
            ny = y + dy[d % 4]
            nx = x + dx[d % 4]
            if 0 <= ny < N and 0 <= nx < M:
                sum_three += arr[ny][nx]
            else:
                break
        else:
            if sum_three > max_sum:
                max_sum = sum_three


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
max_sum = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        check_four(i, j, 1, arr[i][j])
        check_three(i, j)
        visited[i][j] = 0

print(max_sum)
