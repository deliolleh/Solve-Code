def solution(n):
    # 마지막 수 체크를 위한 변수
    total = sum(range(1, n + 1))

    # 삼각형 형태로 array 생성
    arr = [[0] * _ for _ in range(1, n + 1)]

    # 방향 배열
    d = [[1, 0], [0, 1], [-1, -1]]

    # 초기값 초기화
    idx, num, y, x = 0, 1, 0, 0
    while num <= total:
        # y,x 좌표에 num 투입
        arr[y][x] = num

        # 다음 위치 ny, nx 생성
        ny, nx = y + d[idx][0], x + d[idx][1]

        # ny, nx가 범위 밖이면 방향 전환 후 새로운 ny, nx 생성
        if not (0 <= ny < n and 0 <= nx < n and not arr[ny][nx]):
            idx = (idx + 1) % 3
            ny, nx = y + d[idx][0], x + d[idx][1]

        # 새로운 위치 반영
        y, x = ny, nx

        # 넣을 수 증가
        num += 1

    return sum(arr, [])


# --antoher


def solution2(n):
    total = sum(range(1, n + 1))
    arr = [[0] * _ for _ in range(1, n + 1)]
    d = [[1, 0], [0, 1], [-1, -1]]
    idx = 0
    num = 1
    y, x = 0, 0
    while num <= total:
        arr[y][x] = num
        ny, nx = y + d[idx][0], x + d[idx][1]
        if 0 <= ny < n and 0 <= nx < n and not arr[ny][nx]:
            pass
        else:
            idx = (idx + 1) % 3
            ny, nx = y + d[idx][0], x + d[idx][1]
        y, x = ny, nx
        num += 1

    return sum(arr, [])


print(solution(4))
