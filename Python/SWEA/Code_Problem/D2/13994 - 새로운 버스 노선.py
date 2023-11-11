for tc in range(1, int(input()) + 1):
    # 정류장 초기화
    station = [0] * 1001

    # 노선의 수
    N = int(input())
    for i in range(N):
        # 타입, 시작/종점 정류장 위치
        t, s, e = map(int, input().split())

        # 일반 버스
        if t == 1:
            for j in range(s, e + 1):
                station[j] += 1

        # 일반 버스 이외에는 시종점 위치를 먼저 +1 한다
        else:
            station[s] += 1
            station[e] += 1
            # 급행 버스
            if t == 2:
                # 시점 홀수 => s+1 ~ e-1 사이의 홀수 정류장에 정차
                if s % 2:
                    for a in range(s + 1, e):
                        if a % 2 == 1:
                            station[a] += 1

                # 짝수 => 위 조건의 짝수 정류장에만
                else:
                    for b in range(s + 1, e):
                        if b % 2 == 0:
                            station[b] += 1

            # 광역 급행 버스
            else:
                # 홀수 => s+1 ~ e-1 사이에서 3의 배수이면서 10의 배수가 아닌 정류장에 정차
                if s % 2:
                    for c in range(s + 1, e):
                        if c % 3 == 0 and c % 10 != 0:
                            station[c] += 1
                # 짝수 => 같은 조건에 4의 배수의 정류장에 정차
                else:
                    for d in range(s + 1, e):
                        if d % 4 == 0:
                            station[d] += 1

    # 가장 높은 수 => 그 정류장에 많은 노선이 정차한다
    res = max(station)

    print(f'#{tc} {res}')
