from math import isclose

for tc in range(1, int(input()) + 1):
    N = int(input())
    """
    n1 = N ** (1/3)
    n2 = int(round(n1 + 0.1))
    if isclose(n1, n2):
        print(f'#{tc} {n2}')
    else:
        print(f'#{tc} -1')
    """
    '''
    n1 = int(N ** (1/3) - 0.1)
    while n1 ** 3 < N:
        n1 += 1

    if n1 ** 3 == N:
        res = n1
    else:
        res = -1

    print(f'#{tc} {res}')
    '''

    for i in range(1, N+1):
        if i ** 3 == N:
            res = i
            break
        elif i ** 3 > N:
            res = -1
            break

    print(f'#{tc} {res}')
