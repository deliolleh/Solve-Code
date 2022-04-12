def dfs(start, node, eat):
    global res, s_node
    if not edge[node]:
        if eat > res:
            res = eat
            s_node = start
    else:
        for nxt in edge[node]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                dfs(start, nxt, eat + fruit[nxt])
                visited[nxt] = 0


N = int(input())

fruit = [0] + list(map(int, input().split()))

edge = [[] for _ in range(N + 1)]
for m in range(N - 1):
    a, b = map(int, input().split())

    edge[a].append(b)

visited = [0] * (N + 1)
res, s_node = 0, 1
for start in range(1, N + 1):
    visited[start] = 1
    dfs(start, start, fruit[start])
    visited[start] = 0

print(res, s_node)
