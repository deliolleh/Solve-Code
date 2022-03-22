def dfs(n, total):
    global res
    if total > res:
        return
    if n == N:
        if B <= total < res:
            res = total
        return

    dfs(n + 1, total + em[n])
    dfs(n + 1, total)


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    em = list(map(int, input().split()))

    res = 200000

    dfs(0, 0)

    print(f'#{tc} {res - B}')
