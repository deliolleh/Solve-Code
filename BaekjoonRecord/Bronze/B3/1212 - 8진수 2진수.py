import sys
num = list(sys.stdin.readline().rstrip())
N = len(num)
res = 0
for idx in range(N):
    res += int(num[idx]) * 8 ** (N - 1 - idx)

a = list(bin(res))
print(''.join(a[2:]))
