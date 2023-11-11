def check(line):
    level = 1
    prev, need = line[0], 0

    for j in range(1, n):
        now = line[j]
        if need:
            if level >= x * need:
                level, need = 0, 0

        if prev == now:
            level += 1
            if need and level >= x * need:
                level, need = 0, 0
            continue

        elif prev < now:
            if need:
                return 0
            need = now - prev
            if level >= x * need:
                level = 1
                need = 0
            else:
                return 0
        elif prev > now:
            if need:
                return 0
            need = prev - now
            level = 1

        prev = now

    if need:

        return 0
    return 1


for tc in range(1,int(input())+1):
    n, x = map(int,input().split())
    case = [list(map(int,input().split())) for _ in range(n)]
    case2 = list(zip(*case))
    answer = 0

    for i in range(n):
        answer += check(case[i])
        answer += check(case2[i])

    print(f'#{tc} {answer}')