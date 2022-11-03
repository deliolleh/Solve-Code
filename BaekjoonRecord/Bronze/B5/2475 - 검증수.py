A = list(map(int, input().split()))
total = 0

for num in A:
    total += num**2

check_num = total % 10
print(check_num)
