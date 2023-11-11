from collections import deque


def solution(board):
    l = len(board)
    answer = 0
    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

    def bfs(dire):
        used = [[0] * l for _ in range(l)]
        que = deque()
        que.append([0, 0, dire, 0])
        used[0][0] = 1
        while que:
            y, x, ndir, pri = que.popleft()
            if y == l - 1 and x == l - 1:
                return pri
            for d in range(3):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < l and 0 <= ny < l and not used[ny][nx]:
                    used[ny][nx] = 1
                    if not (ndir + d) % 2:
                        que.append([ny, nx, d, pri + 100])
                    else:
                        que.append([ny, nx, d, pri + 500])

    answer = bfs(0)

    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
