import sys


def dfs(ny, nx, cnt):
    # 그냥하면 처음 위치에서도 순회했다고 판단할 수 있어
    # 이를 방지하기 위한 순회횟수 cnt 추가
    # 사이클이 생기려면 4이상이여야하지만 3일때는 불가능하므로 2초과로 범위를 해도 문제 X
    if ny == i and nx == j and cnt > 2:
        print("Yes")
        quit()
    else:
        for d in range(4):
            nny, nnx = ny + dy[d], nx + dx[d]
            # 범위 내 + 색 동일 + 미방문
            if (
                0 <= nny < N
                and 0 <= nnx < M
                and dots[nny][nnx] == dots[ny][nx]
                and not visited[nny][nnx]
            ):
                visited[nny][nnx] = 1
                dfs(nny, nnx, cnt + 1)
                visited[nny][nnx] = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
N, M = map(int, input().split())


dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 이동하면서 계속 dfs => 범위가 50까지라 가까스로 된듯
for i in range(N):
    for j in range(M):
        dfs(i, j, 0)

print("No")
