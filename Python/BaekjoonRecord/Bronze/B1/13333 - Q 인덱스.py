N = int(input())

contents = list(map(int, input().split()))

# q - index
max_q = 0
for i in range(max(contents)):
    # 현재 확인하려하는 Q-index: i
    q_index = i
    # i번 이상의 i번 인용 횟수
    check_up = 0
    # i번 이하의 n-i번 인용 횟수
    check_down = 0
    for idx in range(len(contents)):
        if contents[idx] >= q_index:
            # k 이상
            check_up += 1
        elif contents[idx] <= q_index:
            # n-k이하
            check_down += 1

    # q index: k => k편 이상이 k번이상 인용, N-k편 이하가 k번 이하
    if check_up >= q_index >= check_down:
        max_q = q_index

print(max_q)
