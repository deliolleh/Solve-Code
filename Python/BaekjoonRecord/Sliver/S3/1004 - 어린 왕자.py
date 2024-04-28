from math import sqrt

T = int(input())
for __ in range(T):
    count = 0

    # 출발점/ 도착점 좌표
    x1, y1, x2, y2 = map(int, input().split())

    N = int(input())
    for _ in range(N):
        # 행성계 중심의 좌표, 반지름
        cx, cy, cr = map(int, input().split())

        # 행성계 중심과 각 점까지 거리
        cr1 = sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        cr2 = sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)

        # 두 점 중 하나와 행성계 중심 까지 거리가 행성계 반지름 보다 작으면 통과 해야 함으로 +1
        if (cr1 <= cr < cr2) or (cr2 <= cr < cr1):
            count += 1

    print(count)