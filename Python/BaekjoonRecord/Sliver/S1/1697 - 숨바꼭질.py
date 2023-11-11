from collections import deque

N, K = map(int, input().split())

def solution():
    position = deque()
    position.append([N, 0])
    checked = [0] * 100001

    while position:
        now, count = position.popleft()
        if now == K:
            return count

        # 이동을 할 때 범위 내에서 이동하는지, 이전에 방문한 적이 있는지
        # 왜냐하면 어떤 한 위치 A에 대해 가장 처음 방문하는 경우가 count가 가장 작기 때문이다
        if now + 1 <= 100000 and not checked[now + 1]:
            checked[now + 1] = 1
            position.append([now + 1, count + 1])
        if now - 1 >= 0 and not checked[now - 1]:
            checked[now - 1] = 1
            position.append([now - 1, count + 1])
        if now * 2 <= 100000 and not checked[now * 2]:
            checked[now * 2] = 1
            position.append([now * 2, count + 1])

print(solution())