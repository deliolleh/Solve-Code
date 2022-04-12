from collections import deque


def bfs():
    while que:
        ly, lx, cnt = que.popleft()
        if ly == ey and lx == ex:
            print(cnt)
            return
        for d in range(8):
            ny, nx = ly + dy[d], lx + dx[d]
            if 0 <= ny < L and 0 <= nx < L and not chess[ny][nx]:
                chess[ny][nx] = 1
                que.append([ny, nx, cnt + 1])


dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
TC = int(input())

for tc in range(TC):
    L = int(input())

    chess = [[0] * L for _ in range(L)]

    sy, sx = map(int, input().split())

    ey, ex = map(int, input().split())

    chess[sy][sx] = 1
    que = deque()
    que.append([sy, sx, 0])
    bfs()
