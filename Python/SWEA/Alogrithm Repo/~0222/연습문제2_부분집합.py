# 부분집합의 합이 10이 되는 부분집합을 출력하시오.
arr = [_ for _ in range(1, 11)]
n = len(arr)

count = 0
for i in range(1 << n):
    set_info = []
    for j in range(n):
        if i & (1 << j):
            set_info.append(arr[j])

    sum_i = sum(set_info)
    if sum_i == 10:
        count += 1
        print(*set_info)

print()
print(f'count : {count}')
