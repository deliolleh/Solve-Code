from itertools import permutations

a, b = map(int, input().split())
nums = [i for i in range(1, a + 1)]
result = permutations(nums, b)
for res in result:
    print(*res)