def solution(tickets):
    answer = []
    used = [0] * len(tickets)

    def make_route(route):
        nonlocal answer
        for idx in range(len(tickets)):
            if tickets[idx][0] == route[-1] and not used[idx]:
                used[idx] = 1
                make_route(route + [tickets[idx][1]])
                used[idx] = 0

        if len(route) > len(answer):
            answer = route
        elif len(route) == len(answer):
            for idx2 in range(len(answer)):
                if answer[idx2] != route[idx2]:
                    if sorted([answer[idx2], route[idx2]]) != [answer[idx2], route[idx2]]:
                        answer = route
                    break

    make_route(['ICN'])

    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))