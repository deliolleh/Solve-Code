# 연산 횟수 M
M = int(input())

# 빈 셋 s 생성
s = set()

for i in range(M):
    A, *B = input().split()
    if len(B) != 0:
        num = int(B[0])
    if A == 'add':
        s.add(num)
    elif A == 'remove':
        s.remove(num)
    elif A == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif A == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif A == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif A == 'empty':
        s = set()
