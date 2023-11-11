from collections import deque


def bfs(lo):
    global visited
    visited[lo[0]][lo[1]] = 0
    que = deque()
    que.append(lo)
    while que:
        sy, sx = que.popleft()
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < 5 and 0 <= nx < 4 and arr[ny][nx] != 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[sy][sx] + 1
                que.append([ny, nx])
                if arr[ny][nx] == 2:
                    print(visited[ny][nx])
                    return


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
arr = [[0, 1, 0, 0], [0, 1, 2, 2], [0, 1, 0, 2], [0, 1, 0, 2], [0, 0, 0, 0]]
visited = [[-1] * 4 for _ in range(5)]
start = [1, 0]

bfs(start)
