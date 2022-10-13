def check_leaf_node(now, n):
    global cnt
    if now == n:
        return
    elif not tree[now]:
        cnt += 1
    else:
        for child in tree[now]:
            check_leaf_node(child, n)


N = int(input())

parent = list(map(int, input().split()))
tree = [[] for _ in range(N)]
for idx in range(N):
    if parent[idx] >= 0:
        tree[parent[idx]].append(idx)

remove_node = int(input())

cnt = 0
check_leaf_node(0, remove_node)

print(cnt)
