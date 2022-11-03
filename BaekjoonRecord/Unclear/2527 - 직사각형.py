for tc in range(4):
    income = list(map(int, input().split()))

    a = income[:4]
    b = income[4:]

    if a[0] > b[0]:
        a, b = b, a
