def bfs(i, j):
    que = list()
    visited[i][j] = 1
    que.append([i, j])
    while que:
        sy, sx = que.pop(0)
        for d in range(8):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < col and 0 <= nx < row and arr[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                que.append([ny, nx])


dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
while True:
    row, col = map(int, input().split())
    if col * row == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(col)]
    visited = [[0] * row for _ in range(col)]

    cnt = 0
    for y in range(col):
        for x in range(row):
            if arr[y][x] == 1 and not visited[y][x]:
                cnt += 1
                bfs(y, x)

    print(cnt)
