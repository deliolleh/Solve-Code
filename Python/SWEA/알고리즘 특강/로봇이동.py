def bfs(state):
    que = list()
    que.append(state)
    used[state[0]][state[1]] = 0
    while que:
        sy, sx, di = que.pop(0)

        ny, nx = sy + dy[di], sx + dx[di]
        if 0 <= ny < 4 and 0 <= nx < 3 and not arr[ny][nx] and used[ny][nx] == -1:
            que.append([ny, nx, di])
            used[ny][nx] = used[sy][sx] + 1
            if ny == 3 and nx == 2:
                print(used[ny][nx])
                return
        que.append([sy, sx, 0 if di + 1 == 4 else di + 1])
        que.append([sy, sx, 3 if di - 1 == -1 else di - 1])


dy = [1, 0, -1, 0]
dx = [0, 1, -1, 0]
arr = [
    [0, 1, 1],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 2]
]

start = [0, 0, 2]
used = [[-1] * 3 for _ in range(4)]

bfs(start)
