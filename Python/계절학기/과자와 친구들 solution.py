# 과자와 친구들

import sys; sys.stdin = open('eval_input.txt')
import copy

# N, M, X, Y
N, M, X, Y = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(Y)]

# 8 방향
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

# 횟수 N
for _ in range(N):

    temp = copy.deepcopy(arr)
    small = 100000
    small_arr = []

    for i in range(Y):
        for j in range(X):

            # 과자가 있을 경우
            if arr[i][j]:

                # 내가 먹는 과자
                temp[i][j] -= 1

                # 뺏기는 과자
                for k in range(8):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    # 주변에 과자가 0인 사람 / 과자가 남아있음
                    if 0 <= nx < X and 0 <= ny < Y and not arr[ny][nx] and temp[i][j]:
                        temp[i][j] -= 1

            # 과자가 적은 사람
            if temp[i][j]:

                # 과자 수가 small 값보다 더 적을 경우
                if temp[i][j] < small:
                    # 과자 좌표 갱신
                    small_arr = [[i, j]]
                    # small 값 갱신
                    small = temp[i][j]

                # 과자 수가 small 값과 같을 경우
                elif temp[i][j] == small:
                    # 좌표 추가
                    small_arr.append([i, j])

    # 과자 더하기
    for i, j in small_arr:
        temp[i][j] += M

    # 자리 바꾸기
    for i in range(Y):
        for j in range(X):
            arr[i][j] = temp[i][j-1]

# 출력 값 계산
people = 0
count = 0
most = 0

for i in range(Y):
    for j in range(X):
        if arr[i][j]:
            people += 1
            count += arr[i][j]

            if arr[i][j] > most:
                most = arr[i][j]

print(f'{N}번의 쉬는 시간 후 과자가 남아있는 학생의 인원 수 : {people}')
print(f'남아있는 과자의 총 갯수 : {count}')
print(f'과자가 가장 많이 남은 학생의 과자 개수 : {most}')
print('')
print('[배열]')
for i in range(Y):
    print(*arr[i])