from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(col, row):
    que = deque()
    que.append([col, row])
    visited[col][row] = 1
    while que:
        now = que.popleft()
        for d in range(4):
            ny = now[0] + dy[d]
            nx = now[1] + dx[d]
            if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                que.append([ny, nx])


T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for k in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    print(cnt)
