from collections import deque

N = int(input())

que = deque()
que.append([N, 0])
while que:
    now, cnt = que.popleft()
    if now == 1:
        print(cnt)
        break
    else:
        get = 10**6
        if not now % 2 and get > now // 2:
            que.append([now // 2, cnt + 1])
            get = now // 2
        if not now % 3 and get > now // 3:
            que.append([now // 3, cnt + 1])
        que.append([now - 1, cnt + 1])
