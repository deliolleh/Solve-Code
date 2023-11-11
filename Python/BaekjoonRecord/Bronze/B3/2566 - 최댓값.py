max_col, max_num, max_list = 0, 0, []

for i in range(9):
    now = list(map(int, input().split()))
    max_line = max(now)
    if max_line >= max_num:
        max_col, max_num, max_list = i, max_line, now

max_row = max_list.index(max_num)
print(max_num)
print(max_col + 1, max_row + 1)