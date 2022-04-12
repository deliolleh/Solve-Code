N = int(input())

A = sorted(list(map(int, input().split())))

M = int(input())

B = list(map(int, input().split()))

# 이분탐색해야 풀리는 문제
for b in B:
    l, r = 0, N - 1
    while l <= r:
        middle = (l + r) // 2
        if A[middle] == b:

            print(1)
            break
        elif A[middle] > b:
            r = middle - 1
        else:
            l = middle + 1
    else:
        print(0)
