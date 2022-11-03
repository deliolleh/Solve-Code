# N = int(input())
# i = 1
# cnt = 0
#
# while i <= N:
#     if 1<= i <=99:
#        cnt += 1
#     else:
#         a = i % 10
#         b = (i // 10) % 10
#         c = i // 100
#         if (a-b) == (b-c):
#             cnt +=1
#     i += 1
#
# print(cnt)

N = int(input())

cnt = 0

for num in range(1, N + 1):
    if 1 <= num <= 99:
        cnt += 1
    else:
        num_100 = num // 100
        num_10 = (num % 100) // 10
        num_1 = num % 10
        if (num_100 - num_10) == (num_10 - num_1):
            cnt += 1

print(cnt)
