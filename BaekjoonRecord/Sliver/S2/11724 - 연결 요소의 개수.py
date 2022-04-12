def bfs(node):
    que = list()
    visited[node] = 1
    que.append(node)
    while que:
        now = que.pop(0)
        for n_node in graph[now]:
            if not visited[n_node]:
                visited[n_node] = 1
                que.append(n_node)


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)


for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        cnt += 1
        bfs(i)

print(cnt)
