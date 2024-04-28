# 원의 위치관계에 대해 알아야함

import sys
import math

N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance == 0 and r1 == r2:
        print(-1)

    elif abs(r1 - r2) < distance < abs(r1 + r2):
        print(2)

    elif abs(r1 - r2) == distance or abs(r1 + r2) == distance:
        print(1)

    else:
        print(0)