# arr = [3, 6, 7, 1, 4, 5]
#
# n = len(arr)
# subset = []
#
# for i in range(1 << n):
#     sub_set = []
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=', ')
#             sub_set.append(arr[j])
#     subset.append(sub_set)
#     print()

arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=',')
    print()
