dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(M):
        if arr[y][x] == 2:
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]:
                    arr[ny][nx] = 1

res = 0
for i in range(N):
    res += arr[i].count(0)

print(res)
