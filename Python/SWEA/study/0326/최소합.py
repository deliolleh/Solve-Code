# y 좌표, x 좌표, 현재까지의 합
def find_min(a, b, val):
    global min_sum
    # 좌표를 넘어서면 복귀
    if a >= N or b >= N:
        return
    # 최소합 값을 넘어서도 복귀
    if val > min_sum:
        return
    # 반대편 끝에 도달했을 때 합이 최소일 경우 갱신
    if a == N - 1 and b == N - 1:
        val += arr[a][b]
        if min_sum > val:
            min_sum = val
        return
    # 끝에 도달하지 않았으면 계속 진행
    else:
        find_min(a + 1, b, val + arr[a][b])
        find_min(a, b + 1, val + arr[a][b])


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 10 * N ** 2

    find_min(0, 0, 0)

    print(f'#{tc} {min_sum}')
