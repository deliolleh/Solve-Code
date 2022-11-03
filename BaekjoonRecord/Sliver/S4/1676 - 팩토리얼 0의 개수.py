# 입력받은 수 N
N = int(input())

num_0 = 0

total = 1
while True:
    if N == 0:
        break
    else:
        total *= N
        N -= 1

total_s = str(total)
for idx in range(len(total_s) - 1, 0, -1):
    if total_s[idx] == "0":
        num_0 += 1
    else:
        break

print(num_0)
