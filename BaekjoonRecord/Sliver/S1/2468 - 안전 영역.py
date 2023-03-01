from collections import deque

N = int(input())

area = list()
max_height = 0
for _ in range(N):
    check = list(map(int, input().split()))
    max_height = max(max_height, max(check))
    area.append(check)

res = 0
for height in range(max_height):
    checked = [[0] * N for _ in range(N)]
    now = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > height and not checked[i][j]:
                now += 1
                point = deque()
                point.append([i, j])
                checked[i][j] = 1
                while point:
                    y, x = point.popleft()
                    for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and area[ny][nx] > height and not checked[ny][nx]:
                            checked[ny][nx] = 1
                            point.append([ny, nx])

    res = max(res, now)

print(res)