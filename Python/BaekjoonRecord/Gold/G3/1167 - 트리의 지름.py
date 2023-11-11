from collections import deque


def dfs(n, differ):
    global visited, far_to_root, far_node
    cnt = 0
    for next_tree in tree[n]:
        ne = next_tree[0]
        if visited[ne] == 0:
            visited[ne] = 1
            dfs(ne, differ + next_tree[1])
            visited[ne] = 0
            cnt += 1

    if cnt == 0:
        if differ > far_to_root:
            far_to_root = differ
            far_node = n


def bfs(a):
    que = deque()
    que.append(a)

    while que:
        now = que.popleft()

        for nexts in tree[now]:
            if visited[nexts[0]] == -1:
                visited[nexts[0]] = visited[now] + nexts[1]
                que.append(nexts[0])


V = int(input())

tree = [[] for _ in range(V + 1)]

for v in range(V):
    get = list(map(int, input().split()))

    now = get[0]
    i = 0
    while True:
        if get[2 * i + 1] != -1:
            n_node, distance = get[2 * i + 1], get[2 * i + 2]
            tree[now].append([n_node, distance])
            i += 1
        else:
            break

visited = [0] * (V + 1)
visited[1] = 1
far_to_root = far_node = 0
dfs(1, 0)

visited = [-1] * (V + 1)
visited[far_node] = 0
bfs(far_node)

print(max(visited))
