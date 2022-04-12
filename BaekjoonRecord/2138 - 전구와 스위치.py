import sys

N = int(input())
a = list(map(int, sys.stdin.readline().rstrip()))
b = list(map(int, sys.stdin.readline().rstrip()))
cnt = 0
idx = 0
while a != b:
    if a[idx] != b[idx]:
        cnt += 1
        for i in range(-1, 2):
            if 0 <= idx + i < N:
                a[idx + i] = 1 if a[idx + i] == 0 else 0
    idx = (idx + 1) % N

print(cnt)
