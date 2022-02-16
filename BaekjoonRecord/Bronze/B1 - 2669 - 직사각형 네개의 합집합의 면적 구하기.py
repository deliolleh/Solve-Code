arr = [[0]*100 for _ in range(100)]

for i in range(4):
    sqr = list(map(int, input().split()))
    for row in range(sqr[0], sqr[2]):
        for col in range(sqr[1], sqr[3]):
            arr[col][row] += 1

# for a in arr[-1::-1]:
#     print(*a)

area = 0
for col in range(100):
    for row in range(100):
        if arr[col][row] != 0:
            area += 1

print(area)