def check2(y1, x1, k1):
    for y2 in range(k1):
        for x2 in range(k1):
            if paper[y1 + y2][x1 + x2] == 0:
                return 0
    return 1


def check(y, x, pap):
    global little, cnt
    if pap >= cnt:
        return

    elif x >= 10:
        check(y + 1, 0, pap)

    elif y >= 10:
        cnt = min(cnt, pap)
        return

    elif paper[y][x] == 1:
        for k in range(5, 0, -1):
            if y + k <= 10 and x + k <= 10 and little[k] <= 5:
                if check2(y, x, k):
                    for y1 in range(k):
                        for x1 in range(k):
                            paper[y + y1][x + x1] = 0
                    little[k] += 1
                    check(y, x + 1, pap + 1)
                    for y1 in range(k):
                        for x1 in range(k):
                            paper[y + y1][x + x1] = 1
                    little[k] -= 1

    elif paper[y][x] == 0:
        check(y, x + 1, pap)


paper = [list(map(int, input().split())) for _ in range(10)]

little = [0, 0, 0, 0, 0, 0]

cnt = 26
check(0, 0, 0)

print(cnt if cnt != 26 else -1)
