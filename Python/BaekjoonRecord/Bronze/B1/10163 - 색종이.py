N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for i in range(w):
        for j in range(h):
            arr[y + j][x + i] = n

total = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        total[arr[i][j]] += 1

for idx in range(1, N + 1):
    print(total[idx])
