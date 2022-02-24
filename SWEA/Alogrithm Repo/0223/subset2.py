def f(i, N, s, t):
    global cnt
    cnt += 1
    if s == t:
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()

    elif i == N:
        return
    elif s > t:
        return
    else:
        bit[i] = 1
        f(i + 1, N, s + a[i], t)
        bit[i] = 0
        f(i + 1, N, s, t)


N = 10
a = [x for x in range(1, N + 1)]
bit = [0] * N
cnt = 0
t = 27
f(0, N, 0, t)
print('cnt = ', cnt)
