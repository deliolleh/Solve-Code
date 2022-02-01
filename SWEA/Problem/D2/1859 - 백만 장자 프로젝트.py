# 테스트 케이스
T = int(input())

for _ in range(1, T+1):
    money = 0
    have = 0
    day = int(input())
    price = list(map(int, input().split()))
    for i in range(day):
        if i == day - 1:
            money += abs(price[i]) * have
            break
        if price[i] <= price[i+1]:
            money -= price[i]
            have += 1
        else:
            money += abs(money) * have
            if have > 0:
                have -= 1

    print(f'#{_}, {money}')

# Timeout