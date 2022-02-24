row, col = map(int, input().split())

arr = [[0] * (row + 1) for _ in range(col + 1)]

for i in [0, col]:
    for j in range(row + 1):
        arr[i][j] = 1

for i in [0, row]:
    for j in range(col + 1):
        arr[j][i] = 1

N = int(input())
loc = []

for i in range(N):
    a, b = map(int, input().split())

    if a == 1:
        arr[col][b] += 1
        loc.append([col, b])
    elif a == 2:
        arr[0][b] += 1
        loc.append([0, b])
    elif a == 3:
        arr[b][0] += 1
        loc.append([b, 0])
    else:
        arr[b][row] += 1
        loc.append([b, row])

a, b = map(int, input().split())

def_lo = []
if a == 1:
    arr[col][b] += 2
    def_lo.append([col, b])
elif a == 2:
    arr[0][b] += 2
    def_lo.append([0, b])
elif a == 3:
    arr[b][0] += 2
    def_lo.append([b, 0])
else:
    arr[b][row] += 2
    def_lo.append([b, row])

for lo in loc:
    if def_lo[0] in [1, 2]:
        pass
    else:
        pass
