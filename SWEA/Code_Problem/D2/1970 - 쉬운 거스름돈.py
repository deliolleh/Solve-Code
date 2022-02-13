# Test Case
TC = int(input())

for tc in range(1, TC+1):
    # 받은 돈
    cash = int(input())

    # 순서 출력
    print(f'#{tc}')

    # 50000, 10000, 5000, 1000, 500, 100, 50, 10 순
    money = [0] * 8

    # 10미만의 경우에는 줄 수 있는 동전의 형태가 없으므로 10원 이상일 때만 거스름돈 제공 가능
    while cash >= 10:
        if cash >= 50000:
            money[0] = cash // 50000
            cash %= 50000

        elif cash >= 10000:
            money[1] = cash // 10000
            cash %= 10000

        elif cash >= 5000:
            money[2] = cash // 5000
            cash %= 5000

        elif cash >= 1000:
            money[3] = cash // 1000
            cash %= 1000

        elif cash >= 500:
            money[4] = cash // 500
            cash %= 500

        elif cash >= 100:
            money[5] = cash // 100
            cash %= 100

        elif cash >= 50:
            money[6] = cash // 50
            cash %= 50

        else:
            money[7] = cash // 10
            cash %= 10

    # 리스트를 튜플 형태로
    print(*money)
