N = int(input())

contents = list(map(int, input().split()))

max_q = 0
for i in range(max(contents)):
    q_index = i
    check_up = 0
    check_down = 0
    for idx in range(len(contents)):
        if contents[idx] >= q_index:
            check_up += 1
        else:
            check_down += 1

    if check_up >= q_index >= check_down:
        max_q = q_index

print(max_q)
