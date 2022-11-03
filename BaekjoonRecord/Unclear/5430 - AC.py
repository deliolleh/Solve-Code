from collections import deque
import sys

for tc in range(int(input())):
    p = list(sys.stdin.readline().strip())
    flag = 0

    N = int(input())
    arr = list(input())
    arr = arr[1 : len(arr) - 1]
    if N == 0:
        flag = 1
    if not flag:
        arr = list(map(int, "".join(arr).split(",")))
        que = deque(arr)

        rev = False
        for order in p:
            if order == "R":
                rev = not rev
            elif order == "D" and que:
                if rev:
                    que.pop()
                else:
                    que.popleft()
            else:
                flag = 1
                break

        if rev:
            que = list(que)[::-1]

    if flag:
        print("error")
    else:
        print("[", end="")
        print(*que, sep=",", end="")
        print("]")
