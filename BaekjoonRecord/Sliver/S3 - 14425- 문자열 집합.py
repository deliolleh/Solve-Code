# 집합 S의 수와 검사할 문자열의 수
N, M = map(int, input().split())

# 집합 S에 포함된 문자열 수
num = 0

# 세트로 받았지만 문자열이 여러 번 주어지는 경우는 없으므로 리스트로 받아도 무방
set_S = set()

for i in range(N):
    set_S.add(input())

# 검사하는 문자열들은 따로 할당하지 않고 바로 계산
for j in range(M):
    check = input()

    if check in set_S:
        num += 1

print(num)
