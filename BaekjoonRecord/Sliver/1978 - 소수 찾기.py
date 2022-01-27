# 주어지는 수의 수
N = int(input())

num_list = list(map(int, input().split()))

for num in num_list:
    if num == 1:
        N -= 1
    else:
        i = 1
        while i <= num:
            if i != 1 and i != num and num % i == 0:
                N -= 1
                break
            i += 1

print(N)
