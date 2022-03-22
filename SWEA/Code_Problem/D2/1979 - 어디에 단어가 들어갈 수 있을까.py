TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())
    # 퍼즐 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 빈 칸의 크기가 K인 구역의 수를 입력받을 변수
    cnt = 0
    # 행 체크
    for i in range(N):
        # 각 줄마다 체크하기 위한 변수수
        tem = 0
        for j in range(N):
            if arr[i][j] == 1:
                tem += 1
            # arr[i][j] == 0일 때 그 전까지 빈칸의 크기가 K라면 cnt 증가
            elif tem == K:
                cnt += 1
                tem = 0
            else:
                tem = 0
        # 만약 마지막 줄에 마지막에 0이 없어서 그대로 나왔을 때를 대비
        # K = 3 일 때 0 0 1 1 1이면 증가해야하므로 마지막에 한 번 더 계산
        if tem == K:
            cnt += 1

    # 열 체크
    for i in range(N):
        tem = 0
        for j in range(N):
            if arr[j][i] == 1:
                tem += 1
            elif tem == K:
                cnt += 1
                tem = 0
            else:
                tem = 0

        if tem == K:
            cnt += 1

    print(f'#{tc} {cnt}')
