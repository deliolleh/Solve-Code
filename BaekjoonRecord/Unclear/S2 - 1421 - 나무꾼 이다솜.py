N, C, W = map(int, input().split())

lumbers = []
for idx in range(N):
    lumbers.append(int(input()))

able = min(lumbers)

total = 0
for i in range(1, able + 1):
    tem = 0
    for lumber in lumbers:
        qun = lumber // i
        tem += qun * i * W - ((qun - i) * C)

    if tem > total:
        total = tem

print(total)
