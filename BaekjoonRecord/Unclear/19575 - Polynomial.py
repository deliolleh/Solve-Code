import sys

N, x = map(int, sys.stdin.readline().split())
arr = [0] * (N + 1)
for n in range(N + 1):
    a_i, i = map(int, sys.stdin.readline().split())
    arr[i] = a_i

arr.reverse()
total = arr[0]

for a in arr[1:]:
    total = total * x + a

print(total)

# 순서가 고차항부터 내려온다고 가정했을 때
# import sys
#
# total = 0
# N, x = map(int, sys.stdin.readline().split())
# for n in range(N + 1):
#     a_i, i = map(int, sys.stdin.readline().split())
#     total = total * x + a_i
#
# print(total)
#
