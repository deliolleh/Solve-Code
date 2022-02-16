import sys

day, con = map(int, sys.stdin.readline().split())

day_tem = list(map(int, sys.stdin.readline().split()))

i_tem = 0
for i in range(con):
    i_tem += day_tem[i]

max_tem = 0
for i in range(1, day - con + 1):
    i_tem = i_tem - day_tem[i - 1] + day_tem[i + con - 1]
    if i_tem > max_tem:
        max_tem = i_tem

print(max_tem)
