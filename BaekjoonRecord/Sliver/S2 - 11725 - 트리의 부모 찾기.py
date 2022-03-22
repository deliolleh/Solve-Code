def bfs(now):
    que = [now]
    # 루트의 부모는 0으로 설정
    parent[now] = 0
    while que:
        ch = que.pop(0)
        # 현재 노드와 연결된 노드들 순회 => 부모가 밝혀지지 않은 자녀노드만 추가
        for new in edge[ch]:
            if parent[new] == -1:
                que.append(new)
                # edge[ch]의 부모는 ch
                parent[new] = ch


N = int(input())

# 부모 변수
p = [-1] * (N + 1)
edge = [[] for _ in range(N + 1)]
parent = [-1] * (N + 1)

# 주어진 두 정점 사이의 높이 변화가 1, -1 이므로 둘다 입력
for n in range(N - 1):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)

bfs(1)

for i in range(2, N + 1):
    print(parent[i])
