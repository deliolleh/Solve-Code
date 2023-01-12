from collections import deque

X, Y, Z = map(int, input().split())

total_box = []
ripe = deque()

for iz in range(Z):
    layer_box = []
    for iy in range(Y):
        new = list(map(int, input().split()))
        for ix in range(X):
            if new[ix] == 1:
                ripe.append([iz, iy, ix, 0])
        layer_box.append(new)
    total_box.append(layer_box)

direction = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
days = 0

while ripe:
    z, y, x, day = ripe.popleft()
    if day > days:
        days = day

    for dz, dy, dx in direction:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < Z and 0 <= ny < Y and 0 <= nx < X and not total_box[nz][ny][nx]:
            total_box[nz][ny][nx] = 1
            ripe.append([nz, ny, nx, day + 1])

def check():
    for chz in range(Z):
        for chy in range(Y):
            for chx in range(X):
                if total_box[chz][chy][chx] == 0:
                    return 0
    return 1

print(days) if check() else print(-1)