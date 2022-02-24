'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

arr = [list(map(int, input().split())) for _ in range(5)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 상 하 좌 우
sum_total_4way = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:
                differ = arr[i][j] - arr[ni][nj]
                if differ < 0:
                    differ = differ * (-1)
                sum_total_4way += differ

print(sum_total_4way)

# 8방
sum_total_8way = 0
for i in range(5):
    for j in range(5):
        for k in range(-1, 2):
            for l in range(1, 2):
                differ = arr[i][j] - arr[k][l]
                if differ < 0:
                    differ *= -1
                sum_total_8way += differ

print(sum_total_8way)
