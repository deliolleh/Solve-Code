import sys

day, con = map(int, sys.stdin.readline().split())

day_tem = list(map(int, sys.stdin.readline().split()))

max_tem = 0

for idx1 in range(day-con):
    sum_tem = sum(day_tem[idx1: idx1 + con])

    if sum_tem > max_tem:
        max_tem = sum_tem

print(max_tem)
