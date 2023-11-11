import sys

N, M = map(int, input().split())

woods = list(map(int, sys.stdin.readline().split()))
high = max(woods)
low = 0

while high >= low:
    now = (high + low) // 2
    plan = sum([woods[i] - now if woods[i] > now else 0 for i in range(N)])
    if plan >= M:
        low = now + 1
    else:
        high = now - 1

print(high)