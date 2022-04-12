def bfs(y, x):
    global used, arr
    lst = [[y, x]]
    used[y][x] = 1
    while lst:
        sy, sx = lst.pop(0)
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < 5 and 0 <= nx < 5 and not used[ny][nx]:
                used[ny][nx] = 1
                arr[ny][nx] = arr[sy][sx] + 1
                lst.append([ny, nx])


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
arr = [[0] * 5 for _ in range(5)]
used = [[0] * 5 for _ in range(5)]

arr[2][2] = 1
bfs(2, 2)

for a in arr:
    print(*a)
