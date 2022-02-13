num = [2, 4, 6]

for i1 in num:
    for i2 in num:
        if i1 != i2:
            for i3 in num:
                if i2 != i3 and i2 != i1:
                    print(i1, i2, i3)