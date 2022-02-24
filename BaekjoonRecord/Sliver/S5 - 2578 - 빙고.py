man = [list(map(int, input().split())) for _ in range(5)]

say = []
for _ in range(5):
    say.extend(list(map(int, input().split())))

cnt = 0
for s in say:
    line = 0
    flag = 0
    for row in range(5):
        for col in range(5):
            if man[row][col] == s:
                man[row][col] = 0
                cnt += 1
                flag = 1
                break

        if flag:
            break

    if cnt >= 5:
        for row in range(5):
            if man[row] == [0] * 5:
                line += 1

        for col in range(5):
            tem = []
            for row in range(5):
                tem.append(man[row][col])

            if tem == [0] * 5:
                line += 1

        cross1 = []
        cross2 = []
        for i in range(5):
            cross1.append(man[i][i])
            cross2.append(man[4-i][i])

        if cross1 == [0] * 5:
            line += 1

        if cross2 == [0] * 5:
            line += 1

        if line >= 3:
            print(cnt)
            break
