# 형태가 완전이진트리이다

def solution(n, a, b):
    # 마지막 레벨 idx로 위치 조정
    na = n + a - 1
    nb = n + b - 1

    # 대결횟수
    cnt = 1
    # na == nb: 만났다
    while na != nb:
        na //= 2
        nb //= 2
        cnt += 1

    return cnt

# ---- another


def solution2(n, a, b):
    na = n + a - 1
    nb = n + b - 1

    cnt = 0
    while na != nb:
        na, nb, cnt = na // 2, nb // 2, cnt + 1

    return cnt


print(solution(8, 4, 7))

# 1 2 3 "4" 5 6 7 8 9 10 11 12 13 14 15 "16"
# 1 "4" 5 8 10 12 13 "16"
# "4" 8 12 "16"
# "4" "16"
