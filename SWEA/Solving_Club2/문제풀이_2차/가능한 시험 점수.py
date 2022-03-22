for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))
    subset = [[]]

    for one in score:
        for two in range(len(subset)):
            subset.append(subset[two]+[one])

    subset = set(map(lambda x: sum(x), subset))

    print(f'#{tc} {len(subset)}')

