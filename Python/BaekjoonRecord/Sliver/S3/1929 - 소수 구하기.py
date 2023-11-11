from math import sqrt

A, B = map(int, input().split())

nums = [True] * (B + 1)
nums[0], nums[1] = False, False

for i in range(2, int(sqrt(B)) + 1):
    if nums[i]:
        for j in range(i + i, B + 1, i):
            nums[j] = False

for i in range(A, B + 1):
    if nums[i]:
        print(i)
