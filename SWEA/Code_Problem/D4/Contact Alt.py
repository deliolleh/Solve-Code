from collections import deque

tc = 1
while True:
    try:
        L, S = map(int, input().split())
        edge = list(map(int, input().split()))

        visited = [0] * (max(edge) + 1)
        visited[S] = 1

        res = 0
        que = deque()
        que.append(S)
        while que:
            now = que.popleft()
            if visited[now] > visited[res] or (visited[now] == visited[res] and now > res):
                res = now

            for i in range(0, L, 2):
                if edge[i] == now and not visited[edge[i + 1]]:
                    que.append(edge[i + 1])
                    visited[edge[i + 1]] = visited[now] + 1

        print(f'#{tc} {res}')
        tc += 1

    except:
        break
