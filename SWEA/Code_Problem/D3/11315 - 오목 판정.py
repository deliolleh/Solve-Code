TC = int(input())

for tc in range(1, TC + 1):
    line = int(input())
    flag = 0

    omok = [list(input()) for i in range(line)]

    for idx in range(line):
        count = 0
        for idx2 in range(line):
            if count >= 5:
                flag = 1
                break
            if omok[idx][idx2] == 'o':
                count += 1
            else:
                count = 0

        if count >= 5:
            flag = 1

    if not flag:
        for idx in range(line):
            count = 0
            for idx1 in range(line):
                if count >= 5:
                    flag = 1
                    break
                if omok[idx1][idx] == 'o':
                    count += 1
                else:
                    count = 0

            if count >= 5:
                flag = 1

    if not flag:
        count1 = 0
        count2 = 0
        for idx in range(line):
            if count1 >= 5 or count2 >= 5:
                flag = 1
                break

            if omok[idx][idx] == 'o':
                count1 += 1
            else:
                count1 = 0
            if omok[idx][-1-idx] == 'o':
                count2 += 2
            else:
                count2 = 0

        if count1 >= 5 or count2 >= 5:
            flag = 1

        if count1 >= 5:
            flag = 1
        elif count2 >= 5:
            flag = 1

    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
