res = 0
min_V = 99

for n in range(7):
    a = int(input())
    if a % 2:
        res += a
        if min_V > a:
            min_V = a

if res != 0:
    print(res)
    print(min_V)
else:
    print(-1)
