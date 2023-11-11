change = 1000 - int(input())

coins = 0
for coin in [500, 100, 50, 10, 5, 1]:
    now = change // coin
    change -= now * coin
    coins += now

print(coins)
