def solution(numbers, target):
    answer = 0

    def dfs(now, ssum):
        nonlocal answer
        if now == len(numbers):
            if ssum == target:
                answer += 1
            return
        else:
            dfs(now + 1, ssum + numbers[now])
            dfs(now + 1, ssum - numbers[now])

    dfs(0, 0)
    return answer
