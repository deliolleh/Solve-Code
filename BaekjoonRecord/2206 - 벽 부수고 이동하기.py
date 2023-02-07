import sys

sys.setrecursionlimit(10 ** 4)
N, M = map(int, input().split())

maze = [input() for _ in range(N)]
used = [[0] * M for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = N * M


def solution(y, x, count, poss):
    global maze, used, direction, result
    if y == N - 1 and x == M - 1:
        result = min(result, count)

    elif count > result:
        return

    else:
        for dire in direction:
            ny, nx = y + dire[0], x + dire[1]
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                if maze[ny][nx] == "0":
                    used[ny][nx] = 1
                    solution(ny, nx, count + 1, poss)
                    used[ny][nx] = 0
                elif poss > 0:
                    used[ny][nx] = 1
                    solution(ny, nx, count + 1, poss - 1)
                    used[ny][nx] = 0


solution(0, 0, 1, 1)
print(result) if result != N * M else print(-1)
