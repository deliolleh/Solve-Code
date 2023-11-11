dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(y, x):
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    que = [[y, x]]

    while que:
        cy, cx = que.pop(0)
        if arr[cy][cx] == 3:
            return visited[cy][cx] - visited[y][x] - 1

        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 1 and not visited[ny][nx]:
                que.append([ny, nx])
                visited[ny][nx] = visited[cy][cx] + 1

    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    start = []
    end = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                break

    print(f'#{tc} {bfs(start[0], start[1])}')
