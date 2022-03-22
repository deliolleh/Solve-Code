import sys
sys.setrecursionlimit(10 ** 8)


def dfs(z, c):
    global res
    global flag
    if c == 5:
        res = 1
        flag = 1
        return
    elif not flag:
        for i in nodes[z]:
            if visited[i] == 0 and not flag:
                visited[i] = 1
                dfs(i, c + 1)


N, M = map(int, input().split())

nodes = [[] for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

res = 0
flag = 0
for n in range(N):
    visited = [0] * (N + 1)
    visited[n] = 1
    dfs(n, 1)

print(res)
