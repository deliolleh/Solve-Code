def dfs(n, total):
    global cnt
    if n == N:
        if total == K:
            cnt += 1
        return

    dfs(n + 1, total + num_set[n])
    dfs(n + 1, total)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    num_set = list(map(int, input().split()))

    cnt = 0
    subset = []
    dfs(0, 0)

    print(f'#{tc} {cnt}')
