def perm(n, k):
    if n == k:
        print(*arr)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


arr = [x for x in range(1, 5)]
perm(len(arr), 0)

