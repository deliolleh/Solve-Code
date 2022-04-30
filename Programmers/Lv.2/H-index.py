def solution(citations):
    answer = 0
    # 논문이 최대 h번 인용되려면 h편 이상이여야 함으로
    # h의 최대값은 citations의 크기
    for h in range(1, len(citations) + 1):
        cnt = 0
        # 각 h마다 citation의 인용횟수가 h번 이상이면 cnt 증가
        for idx in range(len(citations)):
            if citations[idx] >= h:
                cnt += 1

        # cnt, 즉 인용된 논문 수가 h 편 이상이면
        # 이 사람의 H-index는 h가 된다
        if cnt >= h:
            answer = h
        # 어긋나면 직전의 h가 이 사람의 최대 H-index이므로
        # 이미 answer
        else:
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
