import sys

N = int(input())

seq = list(map(int, sys.stdin.readline().split()))

max_con = 1
con_sm = 1
con_lg = 1
for idx in range(N-1):
    if seq[idx] < seq[idx+1]:
        con_lg += 1
        if con_sm > max_con:
            max_con = con_sm
        con_sm = 1
    elif seq[idx] > seq[idx+1]:
        con_sm += 1
        if con_lg > max_con:
            max_con = con_lg
        con_lg = 1
    else:
        con_sm += 1
        con_lg += 1

print(max_con)
