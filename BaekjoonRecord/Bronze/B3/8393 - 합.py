A = int(input())

if A < 1 or A > 10000:
    print("error")

else:
    B = 0
    for i in range(1, A + 1):
        B += i
    print(B)
