def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            a = 0 if j >= i else triangle[i - 1][j] + triangle[i][j]
            b = 0 if j - 1 < 0 else triangle[i - 1][j - 1] + triangle[i][j]
            triangle[i][j] = max(a, b)

    answer = max(triangle[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
