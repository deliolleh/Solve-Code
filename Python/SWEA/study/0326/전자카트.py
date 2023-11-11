def shortcut(start, val):
    global visited
    global less_use
    # 사무실을 제외하고 다 돌았을 때
    # 현재 위치로부터 사무실까지의 소비량 더함
    # 이 수치가 가장 적다면 갱신
    if sum(visited) == N - 1:
        val += arr[start - 1][0]
        if less_use > val:
            less_use = val
        return

    # 소비량이 최소소비량 이상이 되면 복귀
    if val > less_use:
        return

    # 현재 방문하지 않은 곳이 있다면
    # 방문처리하고 이동
    # 그 방향으로 다 돌고나면 다른 경로를 계산할 때를 위해
    # 방문처리 취소
    else:
        for dep in range(2, N + 1):
            if visited[dep] == 0:
                visited[dep] = 1
                shortcut(dep, val + arr[start - 1][dep - 1])
                visited[dep] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    less_use = 100 * N ** 2
    visited = [0] * (N + 1)
    shortcut(1, 0)

    print(f'#{tc} {less_use}')
