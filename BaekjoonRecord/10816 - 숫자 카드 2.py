import sys

# 상근이가 가지고 있는 카드 개수
N = int(input())

# 카드의 정보
info = list(sys.stdin.readline().split())

# 정수 M
M = int(input())

# 확인하는 카드 정보
what = list(sys.stdin.readline().split())
result = []
for w in what:
    result.append(str(info.count(w)))

print(' '.join(result))