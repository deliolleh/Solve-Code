from math import sqrt

A, B = map(int, input().split())

nums = [True] * (A + 1)
nums[0], nums[1] = False, False
cnt = 0

for i in range(2, A + 1):
    if nums[i]:
        for j in range(i, A + 1, i):
            if nums[j]:
                nums[j] = False
                cnt += 1
                if cnt == B:
                    print(j)
                    break
