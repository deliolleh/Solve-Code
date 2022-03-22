from collections import deque

N, M = map(int, input().split())

# 순서를 인덱스와 매칭함
arr = deque([i for i in range(1, N + 1)])
wanted = list(map(int, input().split()))
# deque를 쓰지 않고 처리하기 위해 reverse
wanted.reverse()
# deque를 이동하는 횟수를 저장하는 변수
cnt = 0

while wanted:
    # 최상단이 원하는 것일 때 바로 pop
    if arr[0] == wanted[-1]:
        arr.popleft()
        wanted.pop()
    # 아니면 위치가 길이의 절반 미만이면 왼쪽
    # 절반이상이면 오른쪽으로 회전하면서
    # cnt + 1
    elif arr.index(wanted[-1]) > len(arr) // 2:
        arr.appendleft(arr.pop())
        cnt += 1
    else:
        arr.append(arr.popleft())
        cnt += 1

print(cnt)
