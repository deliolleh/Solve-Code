N = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

big_w = 0
big_h = 0
big_w_idx = 0
big_h_idx = 0
for idx in range(6):
    if arr[idx][0] == 1 or arr[idx][0] == 2:
        if arr[idx][1] > big_w:
            big_w = arr[idx][1]
            big_w_idx = idx
    else:
        if arr[idx][1] > big_h:
            big_h = arr[idx][1]
            big_h_idx = idx

small_h = abs(arr[big_w_idx - 1][1] - arr[(big_w_idx + 1) % 6][1])
small_w = abs(arr[big_h_idx - 1][1] - arr[(big_h_idx + 1) % 6][1])
area = big_w * big_h - small_w * small_h
print(area * N)
