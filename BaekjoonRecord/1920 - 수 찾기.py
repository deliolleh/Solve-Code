import sys

N = int(input())

a_list = list(map(int, sys.stdin.readline().split()))

M = int(input())

give_list = list(map(int, sys.stdin.readline().split()))

for one in give_list:
    print(a_list.count(one))