def solution(n):
    answer = [0, 1]
    for n in range(2, n + 1):
        answer.append(answer[n - 1] + answer[n - 2])
    return answer[n] % 1234567


print(solution(3))
