import sys

# 저장된 사이트 수, 찾으려는 사이트 수
N, M = map(int, input().split())

note = dict()

for num in range(N):
    site, pwd = sys.stdin.readline().split()
    note[site] = pwd

for num2 in range(M):
    want = input()
    print(note.get(want))
