E, S, M = map(int, input().split())

# 날짜 계산 변수
e = s = m = 1
# 지구 기준 년도
num = 1
while True:
    # 같아질 때 출력
    if e == E and s == S and m == M:
        print(num)
        break

    # 아니면 1일 증가
    e += 1
    s += 1
    m += 1

    # 범위를 초과했을 때 초기화
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

    num += 1
