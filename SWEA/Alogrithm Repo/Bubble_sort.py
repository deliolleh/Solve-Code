def bubble_sort(a):
    # len(a), len(a)-1, ~ ,1
    for i in range(len(a) - 1, 0, -1):
        # (0 ~ len(a) - 1), (0 ~ len(a) - 2), ~ ,0
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


arr = [55, 7, 13, 49, 30]
bubble_sort(arr)
print(arr)
