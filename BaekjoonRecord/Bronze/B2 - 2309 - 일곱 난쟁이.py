arr = []
flag = 0
for i in range(9):
    arr.append(int(input()))

for i in range(9):
    for j in range(9):
        arr_a = []
        if i != j:
            for k in range(9):
                if k not in [i, j]:
                    arr_a.append(arr[k])

            if sum(arr_a) == 100:
                arr = arr_a
                flag = 1
                break

    if flag:
        break

arr.sort()
for a in arr:
    print(a)
