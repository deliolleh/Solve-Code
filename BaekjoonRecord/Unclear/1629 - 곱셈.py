import sys

A, B, C = map(int, sys.stdin.readline().split())

result = 1
for i in range(B):
    result *= A
    
