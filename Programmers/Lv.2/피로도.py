def solution(k, dungeons):
    answer = 0

    def dfs(stamina, idx, used):
        nonlocal k, answer
        if stamina >= dungeons[idx][0]:
            stamina -= dungeons[idx][1]
            for nidx in range(len(dungeons)):
                if nidx not in used:
                    dfs(stamina, nidx, used + [nidx])
            answer = max(answer, len(used))
        else:
            answer = max(answer, len(used) - 1)

    for nowidx in range(len(dungeons)):
        if dungeons[nowidx][0] <= k:
            dfs(k, nowidx, [nowidx])

    return answer


# print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution(100, [[90, 20], [50, 30], [60, 10], [70, 40], [20, 20]]))
