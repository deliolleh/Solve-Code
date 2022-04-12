num = int(input())
max_len = 1
max_seq = []

if num > 0:
    for first in range(1, num+1):
        arr = [num, first]
        i = 2

        while True:
            new = arr[i - 2] - arr[i - 1]
            if new < 0:
                break

            arr.append(new)
            i += 1

        if len(arr) > max_len:
            max_len = len(arr)
            max_seq = arr

print(max_len)
print(*max_seq)
