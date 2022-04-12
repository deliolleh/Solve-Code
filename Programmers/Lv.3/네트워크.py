def solution(n, computers):
    def bfs(now):
        nonlocal visited
        que = list()
        que.append(now)
        visited[now] = 1
        while que:
            now2 = que.pop(0)
            for link in linked[now2]:
                if not visited[link]:
                    visited[link] = 1
                    que.append(link)

    answer = 0
    linked = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                linked[i].append(j)

    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)

    return answer