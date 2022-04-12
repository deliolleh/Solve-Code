arr = list(input())
cnt = 0
res = 0

for idx in range(len(arr)):
    if arr[idx] == '(':
        if arr[idx] != arr[idx + 1]:
            res += cnt
        else:
            cnt += 1

    else:
        if arr[idx-1] != arr[idx]:
            pass
        else:
            res += 1
            cnt -= 1

print(res)
