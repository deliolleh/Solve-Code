# 테스트 케이스 수
T = int(input())

# 테스트 케이스마다 N,M 입력
for t in range(1, T+1):
    N, M = map(int, input().split())

    # 테스트 케이스 별 영역 입력
    total = []
    for n in range(N):
        total.append(list(map(int, input().split())))

    # 최대 처리한 파리 수를 입력받기 위한 변수
    total_catch = 0
    # 범위는 (전체크기 - 파리채 크기 + 1)
    for idx in range(N-M+1):
        for idx2 in range(N-M+1):
            # idx들이 이동했을 때마다 처리 예상된 파리 수 측정을 위한 변수
            total_tem = 0
            for m in range(M):
                for m2 in range(M):
                    total_tem += total[idx+m][idx2+m2]
            # 기존 최대값보다 최신 결과가 더 많으면 최신 결과를 최대값에 덮어 씌움
            if total_tem > total_catch:
                total_catch = total_tem

    # 최대값을 출력
    print(f'#{t} {total_catch}')
