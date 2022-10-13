N, M = map(int, input().split())


arr1 = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]

if arr1 == arr2:
    print(0)
elif N < 3 and M < 3:
    print(-1)
else:
    cnt = 0
    for i in range(N - 3 + 1):
        for j in range(M - 3 + 1):
            if arr1[i][j] != arr2[i][j]:
                cnt += 1
                for i2 in range(3):
                    for j2 in range(3):
                        if arr1[i + i2][j + j2] == 0:
                            arr1[i + i2][j + j2] = 1
                        else:
                            arr1[i + i2][j + j2] = 0

    if arr1 == arr2:
        print(cnt)
    else:
        print(-1)
