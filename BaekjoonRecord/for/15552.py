import sys

A = int(input())

for i in range(1, A+1) :
    B, C = map(int, sys.stdin.readline().split()) # input과 sys.stdin의 차이
    D = B + C
    print(D)