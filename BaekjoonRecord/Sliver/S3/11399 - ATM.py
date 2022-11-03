import sys

# 사람의 수
N = int(input())

peo = list(map(int, sys.stdin.readline().split()))

peo.sort()

for i in range(len(peo)):
    if i == 0:
        continue
    else:
        peo[i] += peo[i - 1]

print(sum(peo))
