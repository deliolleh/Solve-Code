from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())

arr = list(input().split())
# 알파벳 순으로 정리
arr.sort()

# 조합을 리스트로 받음
kind = list(combinations(arr, L))

# 조합마다 자, 모음 수를 확인하고
# 모음 1자, 자음 2자 이상 있으면 출력
for k in kind:
    vo = 0
    el = 0
    for k2 in k:
        if k2 in vowel:
            vo += 1
        else:
            el += 1

    if vo >= 1 and el >= 2:
        print(*k, sep='')
