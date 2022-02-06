import sys

a, b = map(int, sys.stdin.readline().split())

num_list = [num for num in range(a, b+1) if num == 2 or num % 2 == 1]

num_set = set(num_list)

erase_list = []
for num in range(2, a+1):
    erase_list.extend(range(num*2, b+1, num))
    erase_set = set(erase_list)
    num_set -= erase_set

result = list(num_set)

for res in result:
    print(res)