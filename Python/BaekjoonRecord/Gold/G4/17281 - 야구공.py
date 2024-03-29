def check_get_gain():
    global max_score
    # 현재 타순, 경기 총 점수
    now, score = 0, 0

    # 이닝마다 계산
    for inning in innings:
        # 아웃횟수, 1루, 2루, 3루 배치 상황황
        out, b1, b2, b3 = 0, 0, 0, 0
        # 아웃이 3회가 되기 전에
        while out < 3:
            # 상황
            stage = inning[p[now]]
            # 0 => 아웃
            if stage == 0:
                out += 1

            # 1 => 1루 출루
            elif stage == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2

            # 2 => 2루 출루
            elif stage == 2:
                score += b2 + b3
                b1, b2, b3, = (
                    0,
                    1,
                    b1,
                )

            # 3 => 3루 출루
            elif stage == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1

            # 4 => 홈런
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0

            # 다음 타순
            now = (now + 1) % 9
    max_score = max(max_score, score)


def perm(now):
    global p
    # 모든 타순 배치 완료시
    if now == 9:
        check_get_gain()

    # 4번 타자는 고정되어있음
    elif now == 3:
        p[now] = 0
        perm(now + 1)

    # 나머지 타자 타순 배치
    else:
        for i in range(1, 9):
            if fixed[i] == 0:
                p[now] = i
                fixed[i] = 1
                perm(now + 1)
                fixed[i] = 0


N = int(input())

innings = [list(map(int, input().split())) for _ in range(N)]

# 타순 배열, fixed의 idx번의 야구선수 배정 확인 리스트
p, fixed = [0] * 9, [0] * 9
# 0(1)번 타자가 타순 4번, 0번 타자 사용완료
p[3], fixed[0] = 0, 1
max_score = 0
perm(0)

print(max_score)
