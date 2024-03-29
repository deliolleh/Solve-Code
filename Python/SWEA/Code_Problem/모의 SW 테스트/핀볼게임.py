# 49 / 50 case pass

def check_road(x, y):
    # 남, 동, 북, 서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_sco = 0

    for di in range(4):
        d = di
        nx = x + dx[d]
        ny = y + dy[d]
        sco = 0
        while True:
            # 범위 안에 있을 때
            if 0 <= nx < N and 0 <= ny < N:

                # 블랙홀을 만났을 때
                if arr[ny][nx] == -1:
                    break

                # 시작 위치로 복귀
                elif ny == y and nx == x:
                    break

                # 빈 공간이고 arr 외곽에 있을 때
                # or 들의 묶음은 저기 중 하나만 되면 된다
                elif arr[ny][nx] == 0 and ((nx == 0 and d == 3) or (nx == N - 1 and d == 1) or (ny == 0 and d == 2) or (
                        ny == N - 1 and d == 0)):
                    sco += 1
                    d = (d + 2) % 4

                # 블록들을 만났을 때
                elif arr[ny][nx] in range(1, 6):
                    sim = arr[ny][nx]
                    if sim == 1:
                        if d == 1 or d == 2:
                            d = (d + 2) % 4
                        elif d == 0:
                            d = 1
                        else:
                            d = 2
                    elif sim == 2:
                        if d == 0 or d == 1:
                            d = (d + 2) % 4
                        elif d == 2:
                            d = 1
                        else:
                            d = 0
                    elif sim == 3:
                        if d == 0 or d == 3:
                            d = (d + 2) % 4
                        elif d == 2:
                            d = 3
                        else:
                            d = 0
                    elif sim == 4:
                        if d == 2 or d == 3:
                            d = (d + 2) % 4
                        elif d == 0:
                            d = 3
                        else:
                            d = 2
                    else:
                        d = (d + 2) % 4
                    sco += 1

                # 웜홀을 만났을 때(6 ~ 10)
                elif arr[ny][nx] in range(6, 11):
                    flag = 0
                    for p in range(N):
                        for q in range(N):
                            # 다른 위치 같은 값
                            # 처음에 (p != ny and q != nx)로 했더니
                            # 둘 중 하나만 같은 값이 되어도 통과해버리는 불상사 발생
                            if (p != ny or q != nx) and arr[p][q] == arr[ny][nx]:
                                ny, nx = p, q
                                flag = 1
                                break
                        if flag:
                            break
                nx = nx + dx[d]
                ny = ny + dy[d]

            # 특수 케이스 => 블록에 맞고 외부에 나갔을 때
            else:
                sco += 1
                d = (d + 2) % 4
                nx = nx + dx[d]
                ny = ny + dy[d]

        if sco > max_sco:
            max_sco = sco

    return max_sco


for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                score = check_road(j, i)
                if score > max_score:
                    max_score = score

    print(f'#{tc} {max_score}')
