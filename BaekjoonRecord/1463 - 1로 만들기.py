from collections import deque

N = int(input())

que = deque()
que.append([1, 0])
while que:
    now, cnt = que.popleft()
    if now == N:
        print(cnt)
        break
    else:
        que.append([now * 2, cnt + 1]) if now <= 5 * 10 ** 6 else 1
        que.append([now * 3, cnt + 1]) if now * 3 <= 10 ** 6 else 1
        que.append([now + 1, cnt + 1]) if now <= 10 ** 6 - 1 else 1
