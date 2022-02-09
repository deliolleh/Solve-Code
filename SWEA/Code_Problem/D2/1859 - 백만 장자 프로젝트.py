# 테스트 케이스
T = int(input())

for _ in range(1, T+1):
    # 초기값
    # 소유 중인 돈(-도 포함)
    money = 0
    # 보유 중인 물건의 수
    have = 0

    # 주어진 날
    days = int(input())
    # 각 날의 가격
    price = list(map(int, input().split()))
    # 전체 중 최고가에 팔 때가 가장 이득이 될 때
    max_price = max(price)

    # day+1을 사용하기 위해 days-1 => days-1 일까지 처리
    for day in range(0, days-1):
        if price[day] < max_price:
            money -= price[day]
            have += 1

        # 마지막이 아닌 중간에 최고가가 존재할 때 => 이후의 파트에 대한 최고가를 재할당
        else:
            max_price = max(price[day+1:])
            money += price[day] * have
            have = 0

    # 마지막 날은 전 날에 비해 값이 높을 경우 남은 물건을 팔아야함으로 따로 처리
    # 전 날에 팔았다면 이미 have는 0이므로 의미없음
    money += price[-1] * have

    print(f'#{_} {money}')
