from operator import itemgetter

N = int(input())

order = []
for n in range(N):
    x, y = map(int, input().split())
    order.append([x, y])

order.sort(key=itemgetter(1, 0))

for o in order:
    print(*o)
    