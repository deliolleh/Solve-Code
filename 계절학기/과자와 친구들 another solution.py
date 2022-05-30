from copy import deepcopy


def solution(x, y, n, m, arr):
    di = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for n1 in range(n):
        small = 10000
        temp = deepcopy(arr)
        change = []
        for i in range(y):
            for j in range(x):
                if arr[i][j] != 0:
                    temp[i][j] -= 1
                    hun = 0
                    for d in di:
                        if 0 <= i + d[0] < y and 0 <= j + d[1] < x and not arr[i + d[0]][j + d[1]]:
                            hun += 1

                    if hun > 0:
                        temp[i][j] -= hun

                    if temp[i][j] < 0:
                        temp[i][j] = 0

                    elif temp[i][j] > 0:
                        if temp[i][j] < small:
                            small = temp[i][j]
                            change = [[i, j]]

                        elif temp[i][j] == small:
                            change.append([i, j])

        for ch in change:
            temp[ch[0]][ch[1]] += m

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

    print(f'{50}번의 쉬는 시간 후 과자가 남아있는 학생의 인원 수 : {people}')
    print(f'남아있는 과자의 총 갯수 : {count}')
    print(f'과자가 가장 많이 남은 학생의 과자 개수 : {most}')
    print()

    # cnt, refill, row, col = map(int, input().split())
    # array = [list(map(int, input().split())) for _ in range(col)]
    # print(solution(row, col, cnt, refill, array))

output.close()
