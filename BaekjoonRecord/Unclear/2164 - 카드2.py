N = int(input())

tower = []
for n in range(N, 0, -1):
    tower.append(n)

while len(tower) > 1:
    if len(tower) > 3:
        tower = tower[2::2] + [tower[0]]
    else:
        tower = [tower[0]]

print(*tower)
