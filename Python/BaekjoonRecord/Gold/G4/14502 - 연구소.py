from itertools import combinations
from copy import deepcopy
import sys

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# solution 1
# def solution(arr):
#     while True:
#         change = 0
#         for y in range(N):
#             for x in range(M):
#                 if arr[y][x] == 2:
#                     for dire in direction:
#                         ny, nx = y + dire[0], x + dire[1]
#                         if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]:
#                             arr[ny][nx] = 2
#                             change += 1
#
#         if not change:
#             survive = 0
#             for col in range(N):
#                 survive += arr[col].count(0)
#             return survive

def dfs(arr, check, y, x):
    for dire in direction:
        ny, nx = y + dire[0], x + dire[1]
        if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]:
            arr[ny][nx] = 2
            check[ny][nx] = 1
            dfs(arr, check, ny, nx)

# solution 2
def solution(arr):
    checked = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 2 and not checked[y][x]:
                checked[y][x] = 1
                dfs(arr, checked, y, x)

    count = 0
    for y2 in range(N):
        count += arr[y2].count(0)
    return count


N, M = map(int, input().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
empty = []

for i in range(N):
    for j in range(M):
        if not lab[i][j]:
            empty.append([i, j])

result = 0
todos = combinations(empty, 3)
for todo in todos:
    theory = deepcopy(lab)
    for do in todo:
        theory[do[0]][do[1]] = 1
    result = max(result, solution(theory))

print(result)