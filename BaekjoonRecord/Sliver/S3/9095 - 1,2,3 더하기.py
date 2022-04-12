from collections import deque


def check(start):
    global cnt
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        if now == N:
            cnt += 1
            continue
        for p in range(1, 4):
            if now + p <= N:
                que.append(now + p)


for tc in range(int(input())):
    N = int(input())

    cnt = 0
    for i in range(1, 4):
        check(i)

    print(cnt)
