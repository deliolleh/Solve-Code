import sys

input = sys.stdin

N = int(input.readline())
stairs = []
for _ in range(N):
    stairs.append(int(input.readline()))

dp = [0] * N
dp[0] = stairs[0]
if N > 1:
    dp[1] = dp[0] + stairs[1]
if N > 2:
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]
if N > 3:
    for i in range(3, N):
        dp[i] = max(dp[i - 2], stairs[i - 1] + dp[i - 3]) + stairs[i]

print(dp[-1])