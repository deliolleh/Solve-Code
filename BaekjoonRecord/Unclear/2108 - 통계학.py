import math

N = int(input())

num_list = []

for i in range(5):
    num_list.append(int(input()))

num_list.sort()

print(sum(num_list)//len(num_list))
print(num_list[math.ceil(len(num_list)/2)-1])

mode_set = set()
mode = 0
for num in num_list:
    if mode < num_list.count(num):
        mode = num_list.count(num)
        mode_set = set()
    elif mode == num_list.count(num):
        mode_set.add(num)

mode_list = list(mode_set)
if len(mode_list) == 1:
    print(mode_list[0])
elif len(mode_list) != 0:
    print(mode_list[1])

print(abs(max(num_list)-min(num_list)))