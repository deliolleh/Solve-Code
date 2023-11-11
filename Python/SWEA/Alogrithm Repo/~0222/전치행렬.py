"""
1 2 3
4 5 6
7 8 9
"""

arr = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in arr:
    print(*i)
