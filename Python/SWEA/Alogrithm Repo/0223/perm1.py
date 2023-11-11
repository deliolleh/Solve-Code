def f(i, n):
    if i == n:
        print(p)

    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]


N = int(input())
p = [x for x in range(1, N+1)]
f(0, N)
