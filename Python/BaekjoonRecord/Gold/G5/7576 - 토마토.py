from collections import deque
import sys


def bfs():
    global yet
    max_cnt = 0
    while already:
        sy, sx, cnt = already.popleft()
        max_cnt = cnt if cnt > max_cnt else max_cnt
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < N and 0 <= nx < M and not tomato[ny][nx]:
                tomato[ny][nx] = 1
                already.append([ny, nx, cnt + 1])
                yet -= 1

    # bfs를 다 돌고 난 뒤에도 yet이 0이 아니면 안 익은 부분이 있으므로 -=1 아니면 max_cnt 출력
    print(-1 if yet else max_cnt)
    quit()


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
M, N = map(int, input().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# deque의 초기값을 외부에서 처리
already = deque()
# 배열 값이 0(안 익은 토마토) 수
yet = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            already.appendleft([i, j, 0])
        elif not tomato[i][j]:
            yet += 1

bfs()
