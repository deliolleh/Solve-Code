N = int(input())

arr = [0] * 1000

max_h = 0
max_h_idx = 0
for n in range(N):
    l, h = map(int, input().split())

    arr[l] = h
    if h > max_h:
        max_h = h
        max_h_idx = l

for idx in range(len(arr)-1):
    if idx < max_h_idx and arr[idx] > arr[idx+1]:
        arr[idx+1] = arr[idx]
    elif idx > max_h_idx and arr[idx] < max(arr[idx:]):
        arr[idx] = max(arr[idx:])

print(sum(arr))

