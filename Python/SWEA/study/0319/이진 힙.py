for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    bst = [0] * (N + 1)
    last = 0
    for num in arr:
        last += 1
        bst[last] = num
        c = last
        p = c // 2
        while p >= 1 and bst[p] > bst[c]:
            bst[p], bst[c] = bst[c], bst[p]
            c = p
            p = c // 2

    res = 0
    now = last // 2
    while now >= 1:
        res += bst[now]
        now //= 2

    print(f'#{tc} {res}')
