def swap_check(a):
    global max_eat
    # 색이 다른 두 인접한 칸 선택 => 서로 바꿈
    for i in range(N):
        for j in range(1, N):
            if a[i][j - 1] != a[i][j]:
                a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]

                # 행에 대해 검사
                for k in range(N):
                    con_can = 1
                    for l in range(1, N):
                        if arr[k][l - 1] == arr[k][l]:
                            con_can += 1
                        else:
                            if con_can > max_eat:
                                max_eat = con_can
                            con_can = 1
                    if con_can > max_eat:
                        max_eat = con_can

                # 열에 대해 검사
                other = list(map(list, zip(*a)))
                for k in range(N):
                    con_can = 1
                    for l in range(1, N):
                        if other[k][l - 1] == other[k][l]:
                            con_can += 1
                        else:
                            if con_can > max_eat:
                                max_eat = con_can
                            con_can = 1
                    if con_can > max_eat:
                        max_eat = con_can

                a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]


N = int(input())
arr = [list(input()) for _ in range(N)]
max_eat = 0

# 행 교환 검사
swap_check(arr)
arr = list(map(list, zip(*arr)))
# 열 교환 검사사
swap_check(arr)

print(max_eat)
