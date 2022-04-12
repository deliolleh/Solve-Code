def comparsion(a, b):
    count_a = [0] * 5
    count_b = [0] * 5
    for a1 in range(len(a)):
        count_a[a[a1]] += 1

    for b1 in range(len(b)):
        count_b[b[b1]] += 1

    for j in range(4, -1, -1):
        if count_a[j] > count_b[j]:
            return 'A'
        elif count_a[j] < count_b[j]:
            return 'B'

    return 'D'


N = int(input())

for i in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(comparsion(A[1:], B[1:]))

