import sys

N = int(input())

nums = [0] * 10001

for _ in range(N):
    nums[int(sys.stdin.readline().strip())] += 1

for index in range(10001):
    for period in range(nums[index]):
        print(index)