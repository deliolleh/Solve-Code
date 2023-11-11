# 9번부터 시간 초과
def sum_s(k, arr):
    res2 = 0
    if k == 2:
        res2 = s[arr[0]][arr[1]]
        return res2
    else:
        for t in range(k, N//2):
            arr[t], arr[k] = arr[k], arr[t]
            res2 += sum_s(k+1, arr)
            arr[t], arr[k] = arr[k], arr[t]
    return res2


def perm(n, k):
    global res
    if k == n // 2:
        a, b = sorted(mat[:N // 2]), sorted(mat[N // 2:])
        diff = abs(sum_s(0, a) - sum_s(0, b))
        if res > diff:
            res = diff

    elif mat[0] < N//2:
        for t in range(k, n):
            mat[k], mat[t] = mat[t], mat[k]
            perm(n, k + 1)
            mat[k], mat[t] = mat[t], mat[k]


for tc in range(1, int(input()) + 1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    mat = [i for i in range(N)]

    res = 20000
    perm(N, 0)

    print(f'#{tc} {res}')
