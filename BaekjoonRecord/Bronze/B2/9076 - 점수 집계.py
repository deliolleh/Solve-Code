for tc in range(1, int(input()) + 1):
    score = sorted(list(map(int, input().split())))

    score = score[1:4]
    if max(score) - min(score) >= 4:
        print("KIN")
    else:
        print(sum(score))
