from collections import deque

N = int(input())

grid = []
for _ in range(N):
    grid.append(input())

check = [[0] * N for _ in range(N)]
check_RB = [[0] * N for _ in range(N)]
grid_num = 0
grid_num_RB = 0


def search(how, i, j):
    bot = deque()
    bot.append([i, j])

    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    if how:
        while bot:
            y, x = bot.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not check_RB[ny][nx] and (
                        grid[ny][nx] == grid[i][j] or (grid[i][j] in ["R", "G"] and grid[ny][nx] in ["R", "G"])):
                    check_RB[ny][nx] = 1
                    bot.append([ny, nx])
    else:
        while bot:
            y, x = bot.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not check[ny][nx] and grid[ny][nx] == grid[i][j]:
                    check[ny][nx] = 1
                    bot.append([ny, nx])


for col in range(N):
    for row in range(N):
        if not check[col][row]:
            check[col][row] = 1
            search(0, col, row)
            grid_num += 1
        if not check_RB[col][row]:
            check_RB[col][row] = 1
            search(1, col, row)
            grid_num_RB += 1

print(grid_num, grid_num_RB)
