A, B = map(int, input().split())

if 0 <= B < 45:
    A -= 1
    B += 60

if A == -1:
    A = 23

B -= 45

print("%d %d" % (A, B))
