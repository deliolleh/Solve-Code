for tc in range(1, int(input()) + 1):
    # a, b 숫자열의 수 N, M
    N, M = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 숫자열 곱셈의 덧셈의 최댓값
    max_mul = 0

    # a를 짧은 부분으로 가정하고 계산하기 위해
    # 만약 아니라면 순서를 바꿈
    if N > M:
        N, M = M, N
        a, b = b, a

    # 더 큰 숫자열 위에서 작은 숫자열이 각 index마다 곱하고 더해짐
    for i in range(M - N + 1):
        tem = 0
        for j in range(N):
            tem += a[j] * b[i + j]

        # i위치의 값들을 다 처리하고 나면 그 값이 현재 최대값보다 큰지 비교
        if tem > max_mul:
            max_mul = tem

    print(f'#{tc} {max_mul}')
