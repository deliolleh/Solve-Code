from collections import deque


def dfs(v):
    global visited
    global dfs_list
    for ch in arr[v]:
        if visited[ch] == 0:
            visited[ch] = 1
            dfs_list.append(ch)
            dfs(ch)


def bfs(v):
    visited2 = [0] * (N + 1)
    visited2[v] = 1
    que = deque()
    que.append(v)
    while que:
        now = que.popleft()
        for ch2 in arr[now]:
            if visited2[ch2] == 0:
                visited2[ch2] = 1
                bfs_list.append(ch2)
                que.append(ch2)


N, M, V = map(int, input().split())

arr = [[] for _ in range(N + 1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N + 1):
    arr[i].sort()

dfs_list = []
visited = [0] * (N + 1)
visited[V] = 1
dfs_list.append(V)
dfs(V)
bfs_list = [V]
bfs(V)

print(*dfs_list)
print(*bfs_list)
