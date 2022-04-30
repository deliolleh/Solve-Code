from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = [100000] * (n + 1)
    que = deque()
    que.append(1)
    visited[1] = 1
    while que:
        now = que.popleft()
        for new in graph[now]:
            visited[new] = min(visited[new], visited[now] + 1)
            if visited[new] == visited[now] + 1:
                que.append(new)

    return visited.count(max(visited[1:]))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
