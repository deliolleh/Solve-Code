dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N = int(input())
M = int(input())

arr = [[0] * N for _ in range(N)]

y, x = -1, 0
d = 0
now = N ** 2
while now > 0:
    ny, nx = y + dy[d], x + dx[d]
    if (0 <= ny < N and 0 <= nx < N) and not arr[ny][nx]:
        arr[ny][nx] = now
        now -= 1
        y, x = ny, nx
    else:
        d = (d + 1) % 4

res = [0, 0]
for col in range(N):
    if M in arr[col]:
        res = [col + 1, arr[col].index(M) + 1]
    print(*arr[col])

print(*res)
