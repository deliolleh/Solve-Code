from collections import deque

N = int(input())
a, b = map(int, input().split())
link = int(input())

links = [[0] for _ in range(N + 1)]
for _ in range(link):
    c, d = map(int, input().split())
    links[c].append(d)
    links[d].append(c)

res = -1
people = deque()
people.append([a, 0])
checked = [0] * (N + 1)
checked[a] = 1

while people:
    now, length = people.popleft()
    if now == b:
        res = length
        break
    for i in range(1, len(links[now])):
        if not checked[links[now][i]]:
            checked[links[now][i]] = 1
            people.append([links[now][i], length + 1])

print(res)