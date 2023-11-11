arr = [7, 2, 3, 5, 4, 7]

N = 6

max_arr = arr[0]

for i in range(1, N):
    if arr[i] > max_arr:
        max_arr = arr[i]

print(max_arr)

max_index = []
for j in range(N):
    if arr[j] == max_arr:
        max_index.append(j)

print(*max_index)
