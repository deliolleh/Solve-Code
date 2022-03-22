x, y = map(int, input().split())

n = int(input())
row = [0, x]
col = [0, y]
for i in range(n):
    t, l = map(int, input().split())

    if t == 0:
        col.append(l)

    else:
        row.append(l)

row.sort()
col.sort()
max_size = 0
for idx1 in range(1, len(row)):
    for idx2 in range(1, len(col)):
        area = (row[idx1] - row[idx1 - 1]) * (col[idx2] - col[idx2 - 1])
        if area > max_size:
            max_size = area

print(max_size)
