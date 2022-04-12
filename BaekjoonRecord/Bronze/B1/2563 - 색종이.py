arr = [[0] * 100 for _ in range(100)]

N = int(input())

total = 0

for i in range(N):
    x, y = map(int, input().split())

    for j in range(x, x+10):
        for k in range(y, y+10):
            arr[k][j] += 1

for i in arr:
    for j in range(100):
        if i[j] > 0:
            total += 1

print(total)
