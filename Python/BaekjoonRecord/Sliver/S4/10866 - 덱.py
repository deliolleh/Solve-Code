from collections import deque
import sys

N = int(input())

que = deque()

for n in range(N):
    order = list(sys.stdin.readline().split())

    if "push" in order[0]:
        if "back" in order[0]:
            que.append(order[1])
        else:
            que.appendleft(order[1])

    elif "pop" in order[0]:
        if len(que) == 0:
            print(-1)
        else:
            if "front" in order[0]:
                print(que.popleft())
            else:
                print(que.pop())

    elif "size" in order[0]:
        print(len(que))

    elif "empty" in order[0]:
        if len(que):
            print(0)
        else:
            print(1)

    elif order[0] == "front":
        if not len(que):
            print(-1)
        else:
            print(que[0])

    elif order[0] == "back":
        if not len(que):
            print(-1)
        else:
            print(que[-1])
