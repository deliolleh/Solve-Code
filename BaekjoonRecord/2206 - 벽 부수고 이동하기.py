from collections import deque


def bfs(y, x, crush):
    global visited
    que = deque()
    que.append([y, x, crush])
    visited[y][x] = 1
    while que:
        sy, sx, sc = que.popleft()
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ny, nx = sy + d[0], sx + d[1]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 10 ** 6 and sc + maze[ny][nx] <= 1:
                visited[ny][nx] = min(visited[sy][sx] + 1, visited[ny][nx])
                que.append([ny, nx, sc + maze[ny][nx]])

    return -1 if visited[N-1][M-1] == 10 ** 6 else visited[N-1][M-1]


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
visited = [[10 ** 6] * M for _ in range(N)]

print(bfs(0, 0, 0))
