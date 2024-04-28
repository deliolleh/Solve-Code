from itertools import combinations
answer = 10 ** 9
N = int(input())

# 유저번호를 위한 case
# 이후 풀이과정을 생각하면 범위를 1 ~ N이 아닌 0 ~ N-1로 하는 것이 더 효율적일 것 같음
members = [i for i in range(1, N + 1)]
stat = [list(map(int, input().split())) for _ in range(N)]

# 순서는 필요 없으므로 조합 이용
possibles = combinations(members, N// 2)

for possible in possibles:
    # possibles에서는 N/2 개 만을 뽑으므로 나머지 숫자를 담고 있는 list가 필요함
    another = [x for x in members if x not in possible]

    one = 0
    other = 0
    for mem1 in possible:
        for mem2 in possible:
            one += stat[mem1 - 1][mem2 - 1]

    for mem3 in another:
        for mem4 in another:
            other += stat[mem3 - 1][mem4 - 1]

    if answer > abs(one - other):
        answer = abs(one - other)

print(answer)
