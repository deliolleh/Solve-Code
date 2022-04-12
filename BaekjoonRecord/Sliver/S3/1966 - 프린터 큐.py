from collections import deque
import sys

for tc in range(int(input())):
    # M를 알고싶은 문서의 idx라고 생각함
    N, M = map(int, input().split())

    docu = deque(map(int, sys.stdin.readline().split()))
    cnt = 1

    while True:
        # 가장 앞에 있는 문서의 중요도가 가장 클 때
        if docu[0] >= max(docu):
            # M == 0, 즉 알고싶은 것이 왔으면 cnt를 출력하고 끝냄
            if not M:
                print(cnt)
                break
            # 아니면 cnt + 1
            docu.popleft()
            cnt += 1
            # M이 0에 접근
            M -= 1

        else:
            # 알고싶은 것이 출력되지 못하므로 맨 뒤로
            if not M:
                M = len(docu) - 1
            # 원하는 문서가 앞으로 이동
            else:
                M -= 1
            docu.append(docu.popleft())




