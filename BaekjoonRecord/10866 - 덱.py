from collections import deque

N = int(input())


def do():
    global que
    if 'push' in order[0]:
        if 'back' in order[0]:
            que.append(int(order[1]))
        else:
            que.appendleft(int(order[1]))

    elif 'pop' in order[0]:
        if 'front' in order[0]:
            try:
                pick = que.popleft()
                print(pick)
                return
            except:
                print(-1)
                return
        else:
            try:
                pick = que.pop()
                print(pick)
                return
            except:
                print(-1)
                return
    elif 'size' in order:
        print(len(que))
        return
    elif 'empty' in order:
        if len(que):
            print(0)
        else:
            print(1)
        return
    elif 'front' in order:
        try:
            print(que[0])
        except:
            print(-1)
            return
    elif 'back' in order:
        try:
            print(que[-1])
        except:
            print(-1)
            return


que = deque()
for i in range(N):
    order = input().split()

    do()

