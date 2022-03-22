from collections import deque
import sys

for tc in range(int(input())):
    N, M = map(int, input().split())

    docu = deque(map(int, sys.stdin.readline().split()))
    cnt = 1

    while True:
        if docu[0] >= max(docu):
            if not M:
                print(cnt)
                break
            docu.popleft()
            cnt += 1
            M -= 1

        else:
            if not M:
                M = len(docu) - 1
            else:
                M -= 1
            docu.append(docu.popleft())




