def solution(k, dungeons):
    answer = 0

    def dfs(stamina, idx, used):
        nonlocal k, answer
        # 현재 던전에 필요한 최소 필요도보다 높으면 던전에 들어가고
        # 방문하지 않은 새로운 던전을 찾는다
        if stamina >= dungeons[idx][0]:
            stamina -= dungeons[idx][1]
            for nidx in range(len(dungeons)):
                if nidx not in used:
                    dfs(stamina, nidx, used + [nidx])
            answer = max(answer, len(used))
        # 더이상 방문하지 못했을 때 이번 방문횟수와 이전 방문 중 최댓값을 반영
        else:
            answer = max(answer, len(used) - 1)

    # 모든 던전마다 dfs로 체크
    for nowidx in range(len(dungeons)):
        if dungeons[nowidx][0] <= k:
            dfs(k, nowidx, [nowidx])

    return answer


# print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution(100, [[90, 20], [50, 30], [60, 10], [70, 40], [20, 20]]))
