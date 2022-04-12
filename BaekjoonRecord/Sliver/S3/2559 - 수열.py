import sys

day, con = map(int, sys.stdin.readline().split())

day_tem = list(map(int, sys.stdin.readline().split()))

max_tem = sum(day_tem[0:con])
sum_tem = sum(day_tem[0:con])

for idx1 in range(con, day):
    sum_tem = sum_tem - day_tem[idx1-con] + day_tem[idx1]

    if sum_tem > max_tem:
        max_tem = sum_tem

print(max_tem)
