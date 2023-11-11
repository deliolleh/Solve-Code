import sys


def dfs(now, cnt):
    global visited
    if cnt == 4:
        print(1)
        quit()
    else:
        for friend in people[now]:
            if not visited[friend]:
                visited[friend] = 1
                dfs(friend, cnt + 1)
                visited[friend] = 0


N, M = map(int, input().split())
people = [[] for _ in range(N)]
visited = [0] * N

for m in range(M):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

for n in range(N):
    visited[n] = 1
    dfs(n, 0)
    visited[n] = 0

print(0)
