import sys

x, y = map(int, sys.stdin.readline().split())
arr = [[0] * x for _ in range(y+1)]

N = int(sys.stdin.readline())

for n in range(N):
    a, b = map(int, input().split())

    if a == 0:
        pass
