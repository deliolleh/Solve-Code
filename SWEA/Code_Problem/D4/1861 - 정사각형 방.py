from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def room_find(col, row):
    ret = 0
    visited = [[0] * N for _ in range(N)]
    visited[col][row] = 1

    que = deque()
    que.append([col, row])
    while que:
        now = que.popleft()
        if visited[now[0]][now[1]] > ret:
            ret = visited[now[0]][now[1]]

        for d in range(4):
            if 0 <= now[0] + dy[d] < N and 0 <= now[1] + dx[d] < N and arr[now[0] + dy[d]][now[1] + dx[d]] - \
                    arr[now[0]][now[1]] == 1:
                que.append([now[0] + dy[d], now[1] + dx[d]])
                visited[now[0] + dy[d]][now[1] + dx[d]] = visited[now[0]][now[1]] + 1

    return ret


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = [0, 0]
    for n in range(N):
        for m in range(N):
            cnt = room_find(n, m)
            if cnt > res[1]:
                res = [arr[n][m], cnt]
            elif cnt == res[1] and res[0] > arr[n][m]:
                res = [arr[n][m], cnt]

    print(f'#{tc}', *res)
