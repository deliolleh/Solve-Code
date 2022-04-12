def combin(n, r):
    if n == r:
        sub_set = []
        for i in range(r):
            if check[i] == 1:
                sub_set.append(arr[i])
        print(sub_set)
    else:
        for state in range(2):
            check[n] = state
            combin(n + 1, r)


arr = [1, 2, 3]
check = [0] * len(arr)
combin(0, len(arr))