def solution(n, s, a, b, fares):
    # 무한대
    INF = int(1e9)

    # 연결리스트 => 거리를 무한대로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # 자기자신과의 거리는 0
    for loop in range(n + 1):
        graph[loop][loop] = 0

    # 받은 간선을 graph에 반영
    for dep, arr, differ in fares:
        graph[dep][arr] = differ
        graph[arr][dep] = differ

    # 플로이드 워셜 알고리즘 => 거처가는 경유지를 기준으로 최단거리 측정
    # 경유지 -> 출발지 -> 도착지 순으로 for문 순회
    for m_idx in range(n + 1):
        for d_idx in range(n + 1):
            for a_idx in range(n + 1):
                graph[d_idx][a_idx] = min(graph[d_idx][a_idx], graph[d_idx][m_idx] + graph[m_idx][a_idx])

    # 임의의 경유지 around에 대해, 시작점=> 경유지 => A, B까지의 비용까지의 최소합을 구한다
    answer = int(1e9)
    for around in range(1, n + 1):
        answer = min(answer, graph[s][around] + graph[around][a] + graph[around][b])

    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
