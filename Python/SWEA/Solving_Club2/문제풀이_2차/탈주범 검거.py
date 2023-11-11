def guess_lo(r, c):
    location = 1
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    que = [[r, c]]

    while que:
        col, row = que.pop(0)
        if visited[col][row] == L:
            return location

        for d in range(4):
            nc, nr = col+dy[d], row+dx[d]
            if 0 <= nc < N and 0 <= nr < M and not visited[nc][nr] and\
                    pipe[underground[col][row]][d] and pipe[underground[nc][nr]][opp[d]]:
                que.append([nc, nr])
                visited[nc][nr] = visited[col][row] + 1
                location += 1

    return location


# 이동방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 상 우 하 좌
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]
opp = [2, 3, 0, 1]
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())

    underground = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {guess_lo(R, C)}')
