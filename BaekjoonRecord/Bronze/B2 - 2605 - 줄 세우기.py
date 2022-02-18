N = int(input())
arr = list(map(int, input().split()))

line = [0] * N
for i in range(0, 5):
    if line[N - 1 - arr[i]] == 0:
        line[N - 1 - arr[i]] = i + 1
    else:
        for j in range(N - 1 - arr[i]):
            line[j] = line[j + 1]
        line[N - 1 - arr[i]] = i + 1

print(*line)
