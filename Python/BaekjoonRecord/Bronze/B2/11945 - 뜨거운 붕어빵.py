N, M = map(int, input().split())

bu = [input() for _ in range(N)]
mi = []

for b in bu:
    mi.append(b[-1::-1])

for m in mi:
    print(m)
