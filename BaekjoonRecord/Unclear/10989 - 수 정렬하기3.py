import sys

N = int(input())

arr = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    arr[num] += 1

for idx in range(10001):
    for time in range(arr[idx]):
        print(idx)
