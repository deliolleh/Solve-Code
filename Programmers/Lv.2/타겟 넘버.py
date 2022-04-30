def solution(numbers, target):
    answer = 0

    # 변수: 현재 index/ 현재까지의 합
    def dfs(now, ssum):
        # 함수 안의 함수이므로 nonlocal로 불러옴
        nonlocal answer
        # 배열의 index을 다 돌고 초과 = numbers의 길이
        if now == len(numbers):
            # 이 때 target과 같은 값을 가지면
            # answer 1 증가
            if ssum == target:
                answer += 1
            return
        else:
            # 마지막이 아닐 때
            # 이번 인덱스의 값을 더하는 경우
            dfs(now + 1, ssum + numbers[now])
            # 이번 인덱스의 값을 빼는 경우
            dfs(now + 1, ssum - numbers[now])

    dfs(0, 0)
    return answer
