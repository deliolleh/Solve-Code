def find_tree(now, tree):
    global res
    # 연결된 노드가 없을 때까지 반복
    if now != -1:
        res += 1
        find_tree(tree[now][0], tree)
        find_tree(tree[now][1], tree)


for tc in range(1, int(input()) + 1):
    # Edge의 수 E, 시작할 위치 N
    E, N = map(int, input().split())

    # node 연결에 관한 정보
    pair = list(map(int, input().split()))
    # pair 정보를 담을 node 연결 리스트
    node = [[-1, -1] for _ in range(len(set(pair)) + 1)]

    # 각 노드에 대해
    for n in range(N):
        # 부모 - 자식 노드
        v, c = pair[2*n], pair[2*n+1]
        # 이미 넣은 노드가 있다면 오른쪽, 아니면 왼쪽에 할당
        if node[v][0] == -1:
            node[v][0] = c
        else:
            node[v][1] = c

    # 변수 초기화
    res = 0
    # N가 루트인 서브 트리의 노드 갯수 계산
    find_tree(N, node)

    print(f'#{tc} {res}')
