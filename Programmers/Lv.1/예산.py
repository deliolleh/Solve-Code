def solution(d, budget):
    max_cnt = 0
    for i in range(1 << len(d)):
        sum_d = 0
        cnt = 0
        for j in range(len(d)):
            if i & (1 << j):
                sum_d += d[j]
                cnt += 1

        if sum_d <= budget and cnt >= max_cnt:
            max_cnt = cnt

    return max_cnt


for tc in range(1, int(input())+1):
    a = list(map(int, input().split()))

    b = int(input())

    print(solution(a, b))
