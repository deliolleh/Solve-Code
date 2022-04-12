def bfs(y, x):
    que = list()
    que.append([y, x])
    visited[y][x] = 1
    cnt = 1
    while que:
        sy, sx = que.pop(0)
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and field[ny][nx] and not visited[ny][nx]:
                cnt += 1
                visited[ny][nx] = 1
                que.append([ny, nx])

    return cnt


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
N = int(input())

field = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
res = list()
# 아직 확인하지 않은 아파트 탐색
for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and not visited[i][j]:
            res.append(bfs(i, j))

# 집 수를 오름차순으로 정렬
res.sort()
# 단지 수 우선 출력
print(len(res))
for r in res:
    print(r)
