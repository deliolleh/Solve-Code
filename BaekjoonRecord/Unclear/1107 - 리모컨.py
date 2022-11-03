now = 100
N = input()
M = int(input())

if M == 0:
    choice1 = abs(now - int(N))
    choice2 = len(N)
    print(min(choice2, choice1))
else:
    error_button = list(map(int, input().split()))
    for one in N:
        if int(one) in error_button:
            break
    else:
        print(abs(now - int(N)), len(N))
    less_dist = 500000
    for i in range(0, 500001):
        for j in str(i):
            if j in error_button:
                break
        else:
            less_dist = min(less_dist, abs(int(N) - i))

    for i2 in range(1000000, 500000, -1):
        for j2 in str(i2):
            if j2 in error_button:
                break
        else:
            less_dist = min(less_dist, abs(int(N) - i2))

    print(less_dist)
