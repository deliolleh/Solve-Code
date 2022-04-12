max_peo = 0
peo = 0
for i in range(4):
    out_peo, in_peo = map(int, input().split())

    peo += -out_peo + in_peo

    if peo > max_peo:
        max_peo = peo

print(max_peo)

