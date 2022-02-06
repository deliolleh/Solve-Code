import sys

# 포켓몬 갯수 N, 내가 맞춰야 하는 문제 갯수 M
N, M = map(int, sys.stdin.readline().split())

# 포켓몬 도감/ 0번을 채우지 않기 위해 idx 0에 0 대입
# po_list = [0]
#
# for i in range(N):
#     po_list.append(sys.stdin.readline().rstrip())
#
# for j in range(M):
#     quiz = sys.stdin.readline().rstrip()
#
#     try:
#         quiz_num = int(quiz)
#     except ValueError:
#         print(po_list.index(quiz))
#     else:
#         print(po_list[quiz_num])

po_list = []

for i in range(1, N+1):
    po_list = []