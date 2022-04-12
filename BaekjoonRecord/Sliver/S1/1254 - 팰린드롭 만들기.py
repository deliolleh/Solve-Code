letter = input()

res = letter
i = 1

while True:
    flag = 1
    for j in range(len(res) // 2):
        if res[j] != res[-1 - j]:
            flag = 0
            break

    if flag:
        print(len(res))
        break
    else:
        plus = ''.join(reversed(list(map(str, letter[0:i]))))
        res = letter + plus
        i += 1
