from collections import deque

N = int(input())

card = deque()
# [N, N-1, ..., 2, 1]
for i in range(1, N+1):
    card.appendleft(i)

# 한장 남을 때 까지 반복
while True:
    if len(card) == 1:
        print(*card)
        break

    # 가장 위의 카드를 뽑고
    card.pop()
    # 그 다음 가장 위에 있는 카드를
    tem = card.pop()
    # 맨 밑에 둔다
    card.appendleft(tem)
