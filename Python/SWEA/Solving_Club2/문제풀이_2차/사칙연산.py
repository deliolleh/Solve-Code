def postorder(n):
    if n == -1 or op[n] == '.':
        return
    else:
        if op[n].isnumeric():
            return int(op[n])
        else:
            if op[n] == '+':
                return postorder(ch[n][0]) + postorder(ch[n][1])
            elif op[n] == '-':
                return postorder(ch[n][0]) - postorder(ch[n][1])
            elif op[n] == '*':
                return postorder(ch[n][0]) * postorder(ch[n][1])
            elif op[n] == '/':
                return postorder(ch[n][0]) // postorder(ch[n][1])


for tc in range(1, 11):
    N = int(input())

    op = ['.'] * (N + 1)
    ch = [[-1, -1] for _ in range(N + 1)]

    for i in range(N):
        income = list(input().split())

        idx = int(income[0])
        op[idx] = income[1]
        if len(income) > 2:
            ch[idx][0] = int(income[2])
            ch[idx][1] = int(income[3])

    print(f'#{tc} {postorder(1)}')
