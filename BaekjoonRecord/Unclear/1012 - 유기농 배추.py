TC = int(input())

for tc in range(TC):
    r, c, veg = map(int, input().split())

    field = [[0] * r for _ in range(c)]

    count = 0

    for v in range(veg):
        x, y = map(int, input().split())
        field[y][x] = 1

        if x != 0 and field[y][x - 1] == 1:
            continue
        elif x != r - 1 and field[y][x + 1] == 1:
            continue
        elif y != 0 and field[y - 1][x] == 1:
            continue
        elif y != c - 1 and field[y + 1][x] == 1:
            continue
        else:
            count += 1

    print(count)
