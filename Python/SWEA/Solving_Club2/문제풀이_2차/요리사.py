def sep(n, k, a, b):
    global res
    if n == k:
        if len(a) == len(b):
            a_sum = 0
            b_sum = 0
            for i in a:
                for j in a:
                    a_sum += s[i][j]
            for z in b:
                for y in b:
                    b_sum += s[z][y]
            diff = abs(a_sum - b_sum)
            if res > diff:
                res = diff
        return

    sep(n, k + 1, a + [k], b)
    sep(n, k + 1, a, b + [k])


for tc in range(1, int(input()) + 1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    mat = [i for i in range(N)]

    res = 20000
    sep(N, 0, [], [])

    print(f'#{tc} {res}')
