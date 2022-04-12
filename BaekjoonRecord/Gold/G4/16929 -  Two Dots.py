import sys


def dfs(ny, nx, cnt):
    if ny == i and nx == j and cnt > 2:
        print('Yes')
        quit()
    else:
        for d in range(4):
            nny, nnx = ny + dy[d], nx + dx[d]
            if 0 <= nny < N and 0 <= nnx < M and dots[nny][nnx] == dots[ny][nx] and not visited[nny][nnx]:
                visited[nny][nnx] = 1
                dfs(nny, nnx, cnt + 1)
                visited[nny][nnx] = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
N, M = map(int, input().split())


dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        dfs(i, j, 0)

print('No')
