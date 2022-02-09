# 테스트 케이스
T = int(input())

for _ in range(1, T+1):
    # 초기값
    # 소유 중인 돈(-도 포함)
    money = 0
    # 보유 중인 물건의 수
    have = 0

    # 주어진 날
    day = int(input())
    # 각 날의 가격
    price = list(map(int, input().split()))

    if _ == day-1:
        money += price[_] * have
        break
    else:
        if max(price[_+1:]) > price[_]:
            have += 1
            money -= price[_]
        else:
            money += price[_] * have
            have = 0

    print(f'#{_} {money}')
