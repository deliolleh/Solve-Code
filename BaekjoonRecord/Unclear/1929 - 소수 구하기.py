import sys

a, b = map(int, sys.stdin.readline().split())

now = []
for _ in range(a, b+1):
    now.append(_)

while len(now) != 0:
    count = 0
    for num1 in range(1, now[0]):
        if now[0] % num1 == 0:
            count += 1

    if count == 1:
        print(now[0])
        for num2 in range(a, b+1):
            if num2 % now[0] == 0:
                now.remove(num2)

    now.reverse()
    now.pop()
    now.reverse()

# iso = []
#
# for num in range(a, b + 1):
#     count = 0
#     if num >= 1 and (num == 2 or num % 2 != 0) and num not in iso:
#         for num1 in range(1, num):
#             if num % num1 == 0:
#                 count += 1
#
#         if count == 1:
#             print(num)
#             for num2 in range(a, b+1):
#                 if num2 % num1 == 0:
#                     iso.append(num2)
