from collections import deque
import sys

N = int(input())

que = deque()

for i in range(N):
    # 공백을 기준으로 구분함으로써, push 경우 있는 뒤의 숫자를 한번에 받을 수 있음
    order = list(sys.stdin.readline().split())

    # 입구 좌측, 출구 우측
    if order[0] == "push":
        que.appendleft(int(order[-1]))

    elif order[0] == "pop":
        # pop 시도 => if len(que): print(que.pop())와 동일
        try:
            print(que.pop())
        except:
            print(-1)

    elif order[0] == "size":
        print(len(que))

    elif order[0] == "empty":
        # 비었으면 1, 아니면 0
        if len(que):
            print(0)
        else:
            print(1)

    elif order[0] == "front":
        # que가 비어있지 않으면 출구에 있는 원소 출력
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)

    elif order[0] == "back":
        # 입구에 있는 원소 출력
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
