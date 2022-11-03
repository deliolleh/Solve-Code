# Test case
T = int(input())

for i in range(T):
    B, C = input().split()
    num = int(B)
    for one in C:
        for j in range(num):
            print(one, end="")
    if i != T - 1:
        print()
