def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while p > 0 and tree[c] > tree[p]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = p // 2


def deq():
    global last
    # 루트의 key 값
    tmp = tree[1]
    # 마지막 정점의 키를 루트에 복사
    tree[1] = tree[last]
    last -= 1
    # 부모> 자식 규칙 유지
    p = 1
    # 왼쪽 자식 노드
    c = 2 * p
    # 왼쪽 자식 노드가 없으면 자동으로 오른쪽 자식 노드는 없음
    while c <= last:
        # 오른쪽이 존재하고, 오른쪽이 왼쪽보다 클 때 우측 노드 선택
        if c + 1 <= last and tree[c + 1] > tree[c]:
            c = c + 1
        # 자식의 키 값이 더 크면 교환
        if tree[c] > tree[p]:
            tree[c], tree[p] = tree[p], tree[c]
            p = c
            # c *= 2 도 상관 없을거 같은데
            c = 2 * p
        # 없으면 그만
        else:
            break

    return tmp


# This is max heap
tree = [0] * 101
last = 0
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
# print(tree[1])
enq(9)
# print(tree[1])
while last > 0:
    print(deq(), tree[1])
