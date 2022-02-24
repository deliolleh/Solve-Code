arr = [[] for _ in range(5)]

N = int(input())

for i in range(6):
    a, b = map(int, input().split())
    arr[a].append(b)

print((max(arr[1] + arr[2]) * max(arr[3] + arr[4]) - min(arr[1] + arr[2]) * min(arr[3] + arr[4])) * N)
