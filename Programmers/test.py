def solution(infos, queries):
    answer = []
    people = []
    for info in infos:
        people.append(list(info.split()))

    for query in queries:
        query = list(query.split(" and "))

        while True:
            if "-" not in query:
                break
            query.remove("-")

        for person in people:
            cnt = 0
            for data in query:
                if data not in person:
                    break
            else:
                cnt += 1

            answer.append(cnt)

    return answer


solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
