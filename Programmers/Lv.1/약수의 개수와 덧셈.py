def solution(left, right):
    answer = 0
    for num1 in range(left, right + 1):
        cnt = 0
        for num2 in range(1, num1 + 1):
            if not num1 % num2:
                cnt += 1
        answer = answer - num2 if cnt % 2 else answer + num2
    return answer
