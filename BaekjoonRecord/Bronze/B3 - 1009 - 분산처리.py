for tc in range(int(input())):
    a, b = map(int, input().split())

    total = 1
    for i in range(b):
        total *= a
        if total >= 10:
            total %= 10

    if total == 0:
        total = 10

    print(total)
