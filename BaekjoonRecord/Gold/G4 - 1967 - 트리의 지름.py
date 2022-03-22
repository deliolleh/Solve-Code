import sys
sys.setrecursionlimit(10 ** 8)


def before(num):
    # dfs를 위한 기초작업
    # 끝단 r1, r2를 찾기 위해 초기화하는 작업
    visited = [0] * (N + 1)
    visited[num] = 1
    diff = 0
    r = 0

    def find_long(n, l):
        nonlocal visited
        nonlocal diff
        nonlocal r
        # 리프 노드일 때, l의 크기가 가장 클 때
        if len(no_len[n]) == 1 and l > diff:
            diff = l
            r = n
        else:
            for no, long in no_len[n]:
                # 이동하지 않은 노드들에 대해 순회
                if visited[no] == 0:
                    visited[no] = 1
                    find_long(no, l + long)
    find_long(num, 0)

    return r, diff


N = int(input())

# [연결된 노드, 가중치]로 구성된 리스트
no_len = [[] for _ in range(N + 1)]

for ed in range(N - 1):
    a, b, c = map(int, input().split())
    # 끝단에서 계산하려 함으로 루트방향으로의 방향도 기입
    no_len[a].append([b, c])
    no_len[b].append([a, c])


r_1, long1 = before(1)
r_2, long2 = before(r_1)

print(long2)
