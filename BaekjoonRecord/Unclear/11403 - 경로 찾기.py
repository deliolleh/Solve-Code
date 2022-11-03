N = int(input())

arr = [[1] * N for _ in range(N)]

for n in range(N):
    now = list(map(int, input().split()))
    for idx in range(len(now)):
        if now[idx]:
            arr[n][idx] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[i][j] + arr[j][k] < arr[i][k]:
                arr[i][k] = arr[i][j] + arr[j][k]

for a in arr:
    print(a)
