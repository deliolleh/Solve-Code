import sys

N = int(input())

a_list = list(map(int, sys.stdin.readline().split()))

M = int(input())

give_list = list(map(int, sys.stdin.readline().split()))

for give in give_list:
    print(a_list.count(give))
    for c in range(a_list.count(give)):
        a_list.remove(give)
