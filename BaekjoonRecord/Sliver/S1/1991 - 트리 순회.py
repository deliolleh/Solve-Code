# '.'을 만나면 복귀
def preorder(a):
    global pre
    if a == ".":
        return
    # 아니면 a를 문자열에 더함
    pre += a
    preorder(tree[a][0])
    preorder(tree[a][1])


def inorder(b):
    global ino
    if b == ".":
        return
    inorder(tree[b][0])
    ino += b
    inorder(tree[b][1])


def postorder(c):
    global post
    if c == ".":
        return
    postorder(tree[c][0])
    postorder(tree[c][1])
    post += c


N = int(input())
# 알파벳들을 연결하기 위해 딕셔너리 생성
tree = dict()
for n in range(1, N + 1):
    n1, n2, n3 = input().split()
    # 엣지 연결
    tree[n1] = [n2, n3]

pre = ""
ino = ""
post = ""

preorder("A")
inorder("A")
postorder("A")

print(pre)
print(ino)
print(post)
