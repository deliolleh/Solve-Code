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


# 나이트가 이동할 수 있는 좌표
dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
TC = int(input())

for tc in range(TC):
    # 체스판의 한 변의 길이
    L = int(input())

    chess = [[0] * L for _ in range(L)]

    # 현재 나이트가 있는 칸
    sy, sx = map(int, input().split())

    # 도착지
    ey, ex = map(int, input().split())

    # 출발지 방문체크
    chess[sy][sx] = 1
    que = deque()
    que.append([sy, sx, 0])
    bfs()
