def dfs(k, arr):
    global cnt
    if sum(arr) > k:
        return
    if sum(arr) == k and sorted(arr) not in subset:
        cnt += 1
        subset.append(sorted(arr))
        return

    for i in num_set:
        if i not in arr:
            arr2 = arr + [i]
            dfs(k, arr2)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    num_set = list(map(int, input().split()))

    cnt = 0
    subset = []
    dfs(K, [])

    print(f'#{tc} {cnt}')