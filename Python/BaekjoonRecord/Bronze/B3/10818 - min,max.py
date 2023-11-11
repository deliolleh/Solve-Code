# 이중 for 문으로 했을 때 답은 나오나 시간 초과가 됨
# 생각을 바꿔라 굳이 리스트를 하나하나 찾을 필요가 없었다

A = int(input())
B = list(map(int, input().split()))
max_num = B[0]
min_num = B[0]

# for i in range(A):
#     for j in range(A):
#         if B[i] >= B[j]:
#             c = B[i]
#             B[i] = B[j]
#             B[j] = c
# print(B[4], B[0], sep=' ')

for i in B[1:]:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(min_num, max_num, sep=" ")
