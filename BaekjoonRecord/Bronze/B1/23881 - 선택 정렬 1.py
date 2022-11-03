N, K = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
for i in range(N, 1, -1):
    tar_idx = arr.index(max(arr[:i]))
    arr[tar_idx], arr[i - 1] = arr[i - 1], arr[tar_idx]

    if tar_idx != i - 1:
        cnt += 1

    if cnt == K:
        print(arr[tar_idx], arr[i - 1])

if cnt < K:
    print(-1)
