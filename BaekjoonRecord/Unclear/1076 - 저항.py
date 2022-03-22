total = []

for i in range(3):
    color = input()

    di = color[0:2]

    if di == 'bl':
        if i != 2:
            total.append(0)
        else:
            total.append(10 ** 0)
    elif di == 'br':
        if i != 2:
            total.append(1)
        else:
            total.append(10 ** 1)
    elif di == 're':
        if i != 2:
            total.append(2)
        else:
            total.append(10 ** 2)
    elif di == 'or':
        if i != 2:
            total.append(3)
        else:
            total.append(10 ** 3)
    elif di == 'ye':
        if i != 2:
            total.append(4)
        else:
            total.append(10 ** 4)
    elif di == 'gr':
        if i != 2:
            total.append(5)
        else:
            total.append(10 ** 5)
    elif di == 'bl':
        if i != 2:
            total.append(6)
        else:
            total.append(10 ** 6)
    elif di == 'vi':
        if i != 2:
            total.append(7)
        else:
            total.append(10 ** 7)
    elif di == 'gr':
        if i != 2:
            total.append(8)
        else:
            total.append(10 ** 8)
    elif di == 'wh':
        if i != 2:
            total.append(9)
        else:
            total.append(10 ** 9)

res = (total[0] * 10 + total[1]) * total[2]

print(res)
