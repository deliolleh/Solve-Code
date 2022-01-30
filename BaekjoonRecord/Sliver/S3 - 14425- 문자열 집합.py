# 집합 S의 수와 검사할 문자열의 수
N, M = map(int, input().split())

# 집합 S에 포함된 문자열 수
num = 0

set_S = set()

for i in range(N):
    set_S.add(input())

for j in range(M):
    check = input()

    if check in set_S:
        num += 1

print(num)
