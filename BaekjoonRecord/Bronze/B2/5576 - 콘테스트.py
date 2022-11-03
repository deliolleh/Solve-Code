def top_3():
    total = sorted([int(input()) for _ in range(10)])
    top = total[-1:-4:-1]

    return sum(top)


W = top_3()
K = top_3()

print(W, K)
