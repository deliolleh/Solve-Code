n = int(input())
code_a = sorted(list(map(int, input().split())))
m = int(input())
code_b = list(map(int, input().split()))

res = []
for num in code_b:
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if code_a[mid] == num:
            res.append(1)
            break
        elif code_a[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

    if start > end:
        res.append(0)

print(*res)
