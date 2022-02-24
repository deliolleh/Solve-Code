for tc in range(4):
    income = list(map(int, input().split()))

    A = income[:4]
    B = income[4:]

    for i in range(4):
        if A[i] > B[i]:
            print('a')
        elif A[i] < B[i]:
            print('b')
        else:
            print('same')


