def solution(n, times):
    n -= len(times)
    answer = 0
    lines = times[:]

    while True:
        least = int(10e9)
        index = 0
        lines = list(map(lambda x: x - 1, lines))
        a = lines.index(min(lines))
        b = times.index(min(times))

        choice = a if lines[a] + times[a] < lines[b] + times[b] else b
        lines[choice] += times[choice]
        n -= 1
        answer += 1

        if n == 0:
            answer += max(lines)
            break

    return answer


print(solution(6, [7, 10]))
