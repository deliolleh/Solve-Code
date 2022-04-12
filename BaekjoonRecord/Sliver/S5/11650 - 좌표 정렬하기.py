# Case
N = int(input())
axis = []

for num in range(N):
    axis.append(list(map(int, input().split())))

axis.sort(key=lambda x: (x[0], x[1]))

for here in axis:
    print(*here)