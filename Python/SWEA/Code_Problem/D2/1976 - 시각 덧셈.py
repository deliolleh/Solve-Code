T = int(input())

for t in range(1, T+1):
    total = list(map(int, input().split()))

    # 각 리스트의 시 영역과 분 영역끼리 서로 더함
    clock = total[0] + total[2]
    minute = total[1] + total[3]

    # 조심! 분을 정리하기 전에 시간을 먼저 올려야함(실수한 부분)
    if minute >= 60:
        clock += minute // 60
        minute %= 60

    # 분에서 추가된 시간이 있을 수 있기 때문에 분 이후에 처리/ 시가 0~12 사이이므로 최대 가실 수 있는 경우는 25
    if clock > 24:
        clock -= 24
    elif clock > 12:
        clock -= 12

    print(f'#{t} {clock} {minute}')
