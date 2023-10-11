from collections import deque

A, B = map(int, input().split())

# A -> B로 변환에 성공했는지 체크하는 변수
flag = 0
# queue 이용
que = deque()
# 초기값 입력(초기입력도 횟수에 포함되므로 1)
que.append([A, 1])

while que:
    now, count = que.popleft()

    # 다음 단계 수
    a = 2 * now
    b = int(str(now) + '1')

    # 다음 값이 원하는 값이면 바로 출력하고 break
    # 초기에는 que에 값을 저장한 후 pop했을 때 원하는 값인지 판별하려고 했으나
    # 이로 인한 연산 시간의 추가가 염려 되어 바로 계산하는 형태로 변경(약 12ms 차이 존재)
    if a == B or b == B:
        print(count + 1)
        flag = 1
        break

    # 원하는 값이 없을 경우 queue에 추가
    if a <= B:
        que.append([a, count + 1])
    if b <= B:
        que.append([b, count + 1])

if not flag:
    print(-1)