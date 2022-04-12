N = int(input())

arr = [list(input()) for _ in range(N)]

min_cnt = 1000

while True:
    max_cnt_row = 0
    idx1 = 0
    for i in range(N):
        cnt_row = 0
        for j in range(N):
            if arr[i][j] == 'T':
                cnt_row += 1
        if cnt_row > max_cnt_row:
            max_cnt_row = cnt_row
            idx1 = i

    max_cnt_col = 0
    idx = 0
    for j2 in range(N):
        cnt_col = 0
        for i2 in range(N):
            if arr[i2][j2] == 'T':
                cnt_col += 1
        if cnt_col > max_cnt_col:
            max_cnt_col = cnt_col
            idx = j2

    if max_cnt_row > max_cnt_col:
        for index in range(N):
            arr[idx1][index] = 'T' if arr[idx1][index] == 'H' else 'H'

    else:
        for index2 in range(N):
            arr[index2][idx] = 'T' if arr[index2][idx] == 'H' else 'H'

    change = 0
    for i3 in range(N):
        for j3 in range(N):
            if arr[i3][j3] == 'T':
                change += 1

    if change >= min_cnt:
        print(min_cnt)
        quit()
    else:
        min_cnt = change
