def binary_serach(a, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            # 검색 성공시
            return middle
        # key값이 더 작을 때
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    # 검색 실패시
    return -1


arr = [2, 4, 7, 9, 11, 19, 23]
print(binary_serach(arr, len(arr), 20))
