def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while p and tree[c] > tree[p]:
        if tree[c] > tree[p]:
            tree[c], tree[p] = tree[p], tree[c]
            c = p
            p = p // 2

    print(tree[1:last + 1])


def deq():
    global last
    tem = tree[1]
    tree[1] = tree[last]
    last -= 1

    p = 1
    c = 2 * p
    while c <= last:
        if c + 1 <= last and tree[c+1] > tree[c]:
            c = c+1
        if tree[c] > tree[p]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c *= 2
        else:
            break

    return tem


# 최대힙
# 힙의 원소의 개수
last = 0
tree = [0] * 101
enq(4)
enq(15)
enq(13)
enq(11)
enq(19)
enq(20)
enq(23)
print([deq()])
print(tree[1:last + 1])