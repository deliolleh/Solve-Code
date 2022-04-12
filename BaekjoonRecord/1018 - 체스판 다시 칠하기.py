N, M = map(int, input().split())

chess = [list(input()) for _ in range(N)]

min_repaint = 2500
for i in range(N - 7):
    for j in range(M - 7):
        repaint1 = 0
        for a in range(8):
            for b in range(8):
                if (i + a + j + b) % 2 and chess[i + a][j + b] == chess[i][j]:
                    repaint1 += 1
                elif (i + a + j + b) % 2 == 0 and chess[i + a][j + b] != chess[i][j]:
                    repaint1 += 1

        repaint2 = 0

        min_repaint = min(min_repaint, repaint1 , repaint2)

print(min_repaint)
