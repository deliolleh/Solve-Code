for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0

    for i in range(N):
        for j in range(N):
            # 해설 참고 -> 도시 전체에 서비스가 가능한 영역 K는
            # 도시의 사이즈 N보다 1이 커야한다
            for K in range(1, N + 2):
                cnt = 0
                cost = K * K + (K - 1) * (K - 1)
                for idx1 in range(-K + 1, K):
                    # idx1가 K-1일 때 idx2는 1가지 경우
                    # idx1이 0일때 -k+1 ~ K+1까지, 2k+1가지 경우
                    # idx1이 K+1일 때 idx2는 다시 1가지 경우
                    for idx2 in range(-(K - abs(idx1)) + 1, (K - abs(idx1))):
                        # 확인하고픈 좌표가 arr 좌표계 내이고 그 값이 1일 때 cnt 증가
                        if 0 <= i + idx1 < N and 0 <= j + idx2 < N and arr[i + idx1][j + idx2] == 1:
                            cnt += 1

                # '손해보지 않을때' => 0여도 된다
                if cnt * M - cost >= 0 and cnt > max_cnt:
                    # 처음에 잘못 읽어서 최대 이익인줄;;
                    max_cnt = cnt

    print(f'#{tc} {max_cnt}')
