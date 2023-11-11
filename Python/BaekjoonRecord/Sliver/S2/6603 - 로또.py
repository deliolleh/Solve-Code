from itertools import combinations

while True:
    a, *b = map(int, input().split())
    if not a:
        break

    # 라이브러리 이용
    # choices = combinations(b, 6)
    # for choice in choices:
    #     print(*choice)
    # print()

    def dfs(index, combination):
        if len(combination) == 6:
            print(*combination)

        else:
            for j in range(index + 1, len(b)):
                dfs(j, combination + [b[j]])


    for i in range(len(b) - 5):
        dfs(i, [b[i]])
    print()