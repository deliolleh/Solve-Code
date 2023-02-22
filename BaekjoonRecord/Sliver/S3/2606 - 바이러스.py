from collections import deque

node = int(input())
link = int(input())

links = [[0] for _ in range(node + 1)]
used = [0] * (node + 1)
for _ in range(link):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

virus = deque()
virus.append(1)
used[0], used[1] = 1, 1

while virus:
    now = virus.popleft()
    for i in range(1, len(links[now])):
        connect = links[now][i]
        if not used[connect]:
            used[connect] = 1
            virus.append(connect)

print(sum(used) - 2)
