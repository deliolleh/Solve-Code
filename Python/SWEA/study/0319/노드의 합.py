def find_node(now):
    if now > N:
        return 0
    if tree[now] == 0:
        b = find_node(2 * now)
        a = find_node(2 * now + 1)
        tree[now] = a + b
        return a + b
    else:
        return tree[now]


for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    leaf_node = []
    for m in range(M):
        n, v = map(int, input().split())
        leaf_node.append(n)
        tree[n] = v

    print(f'#{tc} {find_node(L)}')
