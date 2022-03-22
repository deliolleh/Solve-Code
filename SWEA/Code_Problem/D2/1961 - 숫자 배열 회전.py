TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    arr1 = []
    for idx1 in range(N):
        arr_tem = []
        for idx2 in range(N-1, -1, -1):
            arr_tem.append(str(arr[idx2][idx1]))

        arr1.append(arr_tem)

    arr2 = []
    for idx1 in range(N-1, -1, -1):
        arr_tem = []
        for idx2 in range(N-1, -1, -1):
            arr_tem.append(str(arr[idx1][idx2]))
        arr2.append(arr_tem)

    arr3 = []
    for idx1 in range(N-1, -1, -1):
        arr_tem = []
        for idx2 in range(N):
            arr_tem.append(str(arr[idx2][idx1]))
        arr3.append(arr_tem)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr1[i]), ''.join(arr2[i]), ''.join(arr3[i]))
