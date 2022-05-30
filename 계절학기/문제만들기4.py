from copy import deepcopy
import sys; sys.stdin = open('algo_input.txt')

# N, M, X, Y
N, M, X, Y = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(Y)]


def solution(x, y, n, m, arr):
    di = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for n1 in range(n):
        small = 10000
        temp = deepcopy(arr)
        change = []
        for i in range(y):
            for j in range(x):
                if arr[i][j] != 0:
                    temp[i][j] -= 1
                    hun = 0
                    for d in di:
                        if 0 <= i + d[0] < y and 0 <= j + d[1] < x and not arr[i + d[0]][j + d[1]]:
                            hun += 1

                    if hun > 0:
                        temp[i][j] -= hun

                    if temp[i][j] < 0:
                        temp[i][j] = 0

                    elif temp[i][j] > 0:
                        if temp[i][j] < small:
                            small = temp[i][j]
                            change = [[i, j]]

                        elif temp[i][j] == small:
                            change.append([i, j])

        for ch in change:
            temp[ch[0]][ch[1]] += m

        for a in range(y):
            temp[a] = [temp[a][-1]] + temp[a][:x - 1]
        arr = temp
    return arr


print(solution(X, Y, N, M, array))

