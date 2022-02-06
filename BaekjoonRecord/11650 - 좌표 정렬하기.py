# Case
N = int(input())
axis = []

for num in range(N):
    axis.append(list(map(int, input().split())))

for idx in range(1, len(axis)):
    if axis[idx-1][0] > axis[idx][0]:
        axis[idx-1], axis[idx] = axis[idx], axis[idx-1]

for idx3 in range(len(axis)-1):
    if axis[idx3][0] == axis[idx3+1][0] and axis[idx3][1] > axis[idx3+1][1]:
        axis[idx3], axis[idx3+1] = axis[idx3+1], axis[idx3]

for ax in axis:
    for idx in range(len(ax)):
        ax[idx] = str(ax[idx])

    print(' '.join(ax))
