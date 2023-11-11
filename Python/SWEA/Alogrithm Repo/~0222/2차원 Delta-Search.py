"""
3 4
1 2 3 4
5 6 7 8
9 10 11 12
"""
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        print(f'arr[{i}][{j}] = {arr[i][j]}')
        print()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            # 인덱스 체크
            if 0 <= ni < N and 0 <= nj < N:
                print(f'arr[{ni}][{nj}] = {arr[ni][nj]}')

        print('----------------------------')
