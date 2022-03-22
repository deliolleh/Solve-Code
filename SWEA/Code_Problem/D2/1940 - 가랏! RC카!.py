for tc in range(1, int(input()) + 1):
    # Command 수
    N = int(input())
    # 이동거리
    way = 0
    # 속도
    velo = 0

    for i in range(N):
        # 모드/ 가속도
        income = list(map(int, input().split()))

        # income 길이가 1 => 모드 0/ 변화 없음
        if len(income) == 1:
            pass
        # income[0]이 1 => 모드 1/ 가속
        elif income[0] == 1:
            velo += income[1]
        # income[0]이 1 => 모드 2/ 감속
        elif income[0] == 2:
            if velo > 0:
                velo -= income[1]

        # 변화된 속도로 1초간 이동한 거리 추가
        way += velo

    print(f'#{tc} {way}')
