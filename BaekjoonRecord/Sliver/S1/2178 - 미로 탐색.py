def bfs(y, x):
    que = list()
    que.append([y, x])
    visited[y][x] = 1
    while que:
        sy, sx = que.pop(0)
        if sy == N - 1 and sx == M - 1:
            print(visited[sy][sx])
            quit()
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = visited[sy][sx] + 1
                que.append([ny, nx])


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0, 0)
