# 철수 빙고판
man = [list(map(int, input().split())) for _ in range(5)]

# 아나운서 숫자 호명 순서
say = []
for _ in range(5):
    say.extend(list(map(int, input().split())))

# 숫자를 부른 횟수
cnt = 0
for s in say:
    line = 0
    flag = 0
    # 말한 위치에 0으로 체크
    for row in range(5):
        for col in range(5):
            if man[row][col] == s:
                man[row][col] = 0
                cnt += 1
                flag = 1
                break

        if flag:
            break

    # 5개의 숫자를 지고 나서야 빙고 확인이 가능
    if cnt >= 5:
        # 가로 확인
        for row in range(5):
            if man[row] == [0] * 5:
                line += 1

        # 세로 확인
        for col in range(5):
            tem = []
            for row in range(5):
                tem.append(man[row][col])

            if tem == [0] * 5:
                line += 1

        # 대각선 확인
        cross1 = []
        cross2 = []
        for i in range(5):
            cross1.append(man[i][i])
            cross2.append(man[4-i][i])

        if cross1 == [0] * 5:
            line += 1

        if cross2 == [0] * 5:
            line += 1

        # 세 줄 이상 빙고면 호명하고 중단
        if line >= 3:
            print(cnt)
            break
