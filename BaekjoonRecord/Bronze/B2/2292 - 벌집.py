# 입력받은 수
N = int(input())

# 벌집은 1을 제외하고 6씩 증가하는 등차수열이다
cnt = 0

# 1일 땐 자기자신이므로 1 출력
if N == 1:
    print(1)

# 1에서 N까지의 거리는 [3 * (cnt ** 2) - 3 * cnt + 2, 3 * ((cnt+1) ** 2) - 3 * (cnt +1) + 2]에 N이 포함될 때의 cnt + 1 값이다
else:
    while True:
        if N in range(
            3 * (cnt**2) - 3 * cnt + 2, 3 * ((cnt + 1) ** 2) - 3 * (cnt + 1) + 2
        ):
            print(cnt + 1)
            break
        else:
            cnt += 1
