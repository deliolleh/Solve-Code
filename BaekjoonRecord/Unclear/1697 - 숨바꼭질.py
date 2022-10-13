def bfs(goal):
    while road:
        now = road.pop(0)
        if now == goal:
            return visited[now]
        if now - 1 >= 0 and visited[now - 1] == -1:
            visited[now - 1] = visited[now] + 1
            road.append(now - 1)
        if now + 1 <= K and visited[now + 1] == -1:
            visited[now + 1] = visited[now] + 1
            road.append(now + 1)
        if 2 * now <= K and visited[2 * now] == -1:
            visited[2 * now] = visited[now] + 1
            road.append(2 * now)


N, K = map(int, input().split())
visited = [-1] * (max(N, K) + 1)
road = [N]
visited[N] = 0
print(bfs(K))
