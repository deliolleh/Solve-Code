for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    em = list(map(int, input().split()))
    subset = [[]]

    for one in em:
        for push in range(len(subset)):
            subset.append(subset[push] + [one])

    for sub in subset:
        if sum(sub) > B:
            print(f'#{tc} {sum(sub) - B}')
            break

# 메모리 초과