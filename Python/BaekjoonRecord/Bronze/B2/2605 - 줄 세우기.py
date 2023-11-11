N = int(input())

arr = [0] * N

pick = list(map(int, input().split()))

for i in range(N):
    if arr[-1 - pick[i]] != 0:
        for idx in range(1, N - pick[i]):
            arr[idx - 1] = arr[idx]

    arr[-1 - pick[i]] = i + 1

print(*arr)
