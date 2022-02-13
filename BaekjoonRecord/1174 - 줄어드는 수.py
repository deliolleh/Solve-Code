import sys

num = int(sys.stdin.readline())

count = 1
less_num = 0
while count != num:
    state = 0
    less_num += 1
    less_str = str(less_num)
    if len(less_str) > 1:
        for i in range(len(less_str)-1):
            if less_str[i] <= less_str[i+1]:
                state = 1
                break

    if state == 0:
        count += 1

print(less_num)
