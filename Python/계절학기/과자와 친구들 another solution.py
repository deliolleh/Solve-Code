from copy import deepcopy


def solution(x, y, n, m, arr):
    # 8방향
    di = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    # 쉬는 시간 동안
    for n1 in range(n):
        # 과자를 가지고 있는 학생 중 가장 적은 과자 수
        small = 10000
        temp = deepcopy(arr)
        # 가장 적은 과자를 가진 사람(들)
        change = []
        for i in range(y):
            for j in range(x):
                # 과자를 가지고 있으면
                if arr[i][j] != 0:
                    # 일단 하나를 가진다
                    temp[i][j] -= 1
                    # 주위에 과자를 가지고 있지 않은 사람
                    hun = 0
                    for d in di:
                        if 0 <= i + d[0] < y and 0 <= j + d[1] < x and not arr[i + d[0]][j + d[1]]:
                            hun += 1

                    if hun > 0:
                        temp[i][j] -= hun

                    # 과자를 다 먹었다면 0으로 초기화
                    if temp[i][j] < 0:
                        temp[i][j] = 0

                    # 과자가 남아있다면
                    elif temp[i][j] > 0:
                        # 현재 남은 과자가 small보다 작은 경우
                        if temp[i][j] < small:
                            # 새로운 small 갱신, change 초기화
                            small = temp[i][j]
                            change = [[i, j]]

                        # small과 같다면 change에 추가
                        elif temp[i][j] == small:
                            change.append([i, j])

        # change의 사람들에게 과자 추가
        for ch in change:
            temp[ch[0]][ch[1]] += m

        # 오른쪽으로 한칸씩 이동
        for a in range(y):
            temp[a] = [temp[a][-1]] + temp[a][:x - 1]
        arr = temp

    return arr


file = open('eval_input.txt', 'r', encoding='utf8')
output = open('eval_output.txt', 'w')
for test in range(50):
    cnt, refill, row, col = map(int, file.readline().split())
    array = [list(map(int, file.readline().split())) for _ in range(col)]
    result = solution(row, col, cnt, refill, array)
    people = row * col - sum(result, []).count(0)
    count = sum(sum(result, []))
    most = max(sum(result, []))
    output.write(str(people) + ' ' + str(count) + ' ' + str(most) + '\n')
    print(people, count, most)

    # print(f'{50}번의 쉬는 시간 후 과자가 남아있는 학생의 인원 수 : {people}')
    # print(f'남아있는 과자의 총 갯수 : {count}')
    # print(f'과자가 가장 많이 남은 학생의 과자 개수 : {most}')
    # print()

output.close()
