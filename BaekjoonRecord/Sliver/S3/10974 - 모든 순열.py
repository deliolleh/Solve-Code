def perm(now, end, li):
    global visited
    # N자리 순열을 만들어놓았으면
    # li를 출력
    if now == end:
        print(*li)
    else:
        # 1 ~ N까지 순환하면서
        # visited에 사용되지 않은 수를 li에 포함시키고
        # visited에 추가하고 진행
        # 다 진행하고 나면 visited를 해제함
        for i in range(1, N + 1):
            if visited[i] == 0:
                visited[i] = 1
                perm(now + 1, end, li + [i])
                visited[i] = 0


N = int(input())

# 1 ~ N까지의 visited 생성
visited = [0] * (N + 1)

# 순열 생성
perm(0, N, [])
