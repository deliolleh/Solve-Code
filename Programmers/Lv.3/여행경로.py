def solution(tickets):
    answer = []
    used = [0] * len(tickets)

    def make_route(route):
        nonlocal answer
        # 다음 도착 장소 선택 => 재귀
        for idx in range(len(tickets)):
            if tickets[idx][0] == route[-1] and not used[idx]:
                used[idx] = 1
                make_route(route + [tickets[idx][1]])
                used[idx] = 0

        # for 문을 나왔을 때 => answer에 있는 루트의 길이보다 더 길면 바로 업데이트
        if len(route) > len(answer):
            answer = route

        # 같은 경우에는 알파벳순서가 더 빠른 쪽이 answer
        elif len(route) == len(answer):
            for idx2 in range(len(answer)):
                if answer[idx2] != route[idx2]:
                    if sorted([answer[idx2], route[idx2]]) != [answer[idx2], route[idx2]]:
                        answer = route
                    break

    make_route(['ICN'])

    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))