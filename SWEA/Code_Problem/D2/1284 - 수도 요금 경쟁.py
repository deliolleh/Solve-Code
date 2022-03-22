for tc in range(1, int(input()) + 1):
    # A사 리터당 요금/ B사 기본요금 / B사 기본요금 최대사용량 / B사 리터당 요금 / 한달 수도사용량
    P, Q, R, S, W = map(int, input().split())

    # W 리터를 썼을 때의 A사 요금
    p_pay = P * W

    # W가 R보다 적으면 B사는 기본요금만 낸다
    if W <= R:
        q_pay = Q
    # R보다 많으면, B사의 기본요금 + (사용량 - 기본용량) * B사 리터당 요금
    else:
        q_pay = Q + (W-R) * S

    # 더 작은 요금 출력력
    print(f'#{tc} {min(p_pay, q_pay)}')
