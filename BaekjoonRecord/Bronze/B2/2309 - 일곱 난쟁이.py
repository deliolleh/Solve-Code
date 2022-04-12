arr = []
flag = 0
for i in range(9):
    arr.append(int(input()))

# 포함시키지 않을 두 난쟁이 선택
for i in range(9):
    for j in range(9):
        arr_a = []
        if i != j:
            # 나머지 난쟁이들의 키를 모음
            for k in range(9):
                if k not in [i, j]:
                    arr_a.append(arr[k])

            # 그 키가 100이면 flag을 세우고 키들의 배열을 외부에 저장
            if sum(arr_a) == 100:
                arr = arr_a
                flag = 1
                break

    if flag:
        break

# 오름차순 정렬
arr.sort()
for a in arr:
    print(a)
