import sys

card = dict()
N = int(input())

for num in list(sys.stdin.readline().split()):
    if card.get(num) == None:
        card[num] = 1
    else:
        card[num] += 1

M = int(input())

for num2 in list(sys.stdin.readline().split()):
    print(card.get(num2, 0))
