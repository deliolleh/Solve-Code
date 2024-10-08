R, C, K = map(int, input().split())

# K = 1 이면 항상 가능
if K == 1:
    print(1)

# 가로 세로 중 하나라도 길이가 1이면
# 다른 하나가 2의 배수일 때만 K가 어떤 값을 가지든 방문가능하다
# 나머지는 불가
elif R == 1 or C == 1:
    if not (R * C) % 2:
        print(1)
    else:
        if K == 1:
            print(1)
        else:
            print(0)

# 2 * 2 구조에서는 언제나 가능
elif not (R * C) % 2:
    print(1)

# 가로 세로 둘 다 2 초과일 때
else:
    print(0)