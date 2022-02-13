import sys

A, B, C = map(str, sys.stdin.readline().split())

check = len(C)

A = int(A[-check:])
B = int(B[-check:])
C = int(C)

print((A * B) % C)
