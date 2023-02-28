N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i, j = 0, 0
res = []
while i < N and j < M:
    if arr1[i] >= arr2[j]:
        res.append(arr2[j])
        j += 1
    else:
        res.append(arr1[i])
        i += 1

if i < N:
    res += arr1[i:]
else:
    res += arr2[j:]

print(*res)