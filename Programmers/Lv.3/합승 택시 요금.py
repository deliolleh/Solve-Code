def solution(n, s, a, b, fares):
    answer = 0
    link = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        link[c].append([d, f])
        link[d].append([c, f])

    short_way = []
    for arrive in [a, b]:
        arr = []
        less_cash = [10**10]
        visited = [0] * (n + 1)
        visited[s] = 1

        def dfs(array, total):
            nonlocal less_cash, arr
            if array[-1] == arrive:
                if sum(less_cash) > sum(total):
                    less_cash = total
                    arr = array
            else:
                for node in link[array[-1]]:
                    if not visited[node[0]]:
                        visited[node[0]] = 1
                        dfs(array + [node[0]], total + [node[1]])

        dfs([s], [])
        short_way.append([arr, less_cash])

    if len(short_way[0]) > len(short_way[1]):
        short_way[0], short_way[1] = short_way[1], short_way[0]

    differ = 0
    for idx in range(1, len(short_way[0][0])):
        if short_way[0][0][idx] != short_way[1][0][idx]:
            answer += sum(short_way[0][1][idx - 1 :]) + sum(short_way[1][1][idx - 1 :])
            break
        else:
            answer += short_way[0][1][idx - 1]
    else:
        answer += short_way[1][1][len(short_way[0]) - 1 :]

    return answer


print(
    solution(
        6,
        4,
        6,
        2,
        [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
    )
)
