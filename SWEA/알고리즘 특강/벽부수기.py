def bfs(y, x, cnt):
    que = list()
    que.append([y, x, cnt])
    visited[y][x] = 0
    while que:
        sy, sx, sc = que.pop(0)
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == -1 and sc + arr[ny][nx] < 3:
                visited[ny][nx] = visited[sy][sx] + 1
                if ny == nx == 4:
                    return visited[ny][nx]
                que.append([ny, nx, sc + arr[ny][nx]])
    return -1


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
arr = [
    [2, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0]
]

visited = [[-1] * 5 for _ in range(5)]

print(bfs(0, 0, 0))
