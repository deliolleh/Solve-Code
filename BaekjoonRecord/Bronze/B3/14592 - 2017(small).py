
N = int(input())

pati = list()
for num in range(N):
    info = list(map(int, input().split()))
    info.append(num + 1)
    pati.append(info)

pati.sort(key=lambda x: (-x[0], x[1], x[2]))

print(pati[0][-1])
