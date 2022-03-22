def check_omok(o):
    for j in range(19):
        for i in range(19):
            if o[j][i] != 0:
                if i <= 14:
                    check = 0
                    a = 1
                    while True:
                        if i + a >= 19:
                            break
                        elif o[j][i + a] != o[j][i]:
                            break
                        else:
                            check += 1
                            a += 1
                    if check == 4:
                        return o[j][i], j, i

                if j <= 14:
                    check = 0
                    b = 1
                    while True:
                        if i + b >= 19:
                            break
                        elif o[j + b][i] != o[j][i]:
                            break
                        else:
                            check += 1
                            b += 1
                    if check == 4:
                        return o[j][i], j, i

                if i <= 13 and j <= 13:
                    check = 0
                    c = 1
                    while True:
                        if i + c >= 19 or j + c >= 19:
                            break
                        elif o[j + c][i + c] != o[j][i]:
                            break
                        else:
                            check += 1
                            c += 1
                    if check == 4:
                        return o[j][i], j, i

    return 0, 0, 0


omok = [list(map(int, input().split())) for _ in range(19)]

a, b, c = check_omok(omok)

if a != 0:
    print(a)
    print(b + 1, c + 1)
else:
    print(a)
