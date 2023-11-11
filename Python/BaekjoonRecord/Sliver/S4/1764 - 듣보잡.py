import sys

# 듣도 못한 N, 보도 못한 M
N, M = map(int, sys.stdin.readline().split())

no_listen = set()
no_see = set()
no_lis_see = set()

for idx in range(N):
    no_listen.add(sys.stdin.readline().rstrip())

for idx2 in range(M):
    no_see.add(sys.stdin.readline().rstrip())

no_lis_see = sorted(no_listen & no_see)

print(len(no_lis_see))
for thumb_up in no_lis_see:
    print(thumb_up)

# 인터넷 참고했음 - set의 교집합 구하는 방법
