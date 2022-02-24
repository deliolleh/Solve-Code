N, K = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
flag = 0
for i in range(N, 1, -1):
    for j in range(i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            cnt += 1

        if cnt == K:
            print(arr[j], arr[j + 1])
            flag = 1
            break

    if flag == 1:
        break

if cnt < K:
    print(-1)
