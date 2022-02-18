first = int(input())

max_con = 0
max_seq = []
for num in range(first - 1, 0, -1):
    arr = [first, num]
    i = 1
    while True:
        arr.append(arr[i-1] - arr[i])
        if arr[-1] < 0:
            arr = arr[:len(arr)-1]
            break
        i += 1

    if len(arr) >= max_con:
        max_con = len(arr)
        max_seq = arr

print(max_con)
print(*max_seq)
