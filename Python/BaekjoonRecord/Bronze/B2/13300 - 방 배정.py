N, K = map(int, input().split())

arr = [[0] * 2 for _ in range(7)]

for i in range(N):
    s, g = map(int, input().split())

    arr[g][s] += 1

least_room = 0

for row in range(7):
    for col in range(2):
        if arr[row][col] % K != 0:
            least_room += (arr[row][col]) // K + 1
        else:
            least_room += (arr[row][col]) // K

print(least_room)
