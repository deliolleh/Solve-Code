T = int(input())

wanted = [int(input()) for _ in range(T)]
end = max(wanted)

dp = [[0, 0] for _ in range(end + 1)]
dp[0][0] = 1
if end > 0:
    dp[1][1] = 1

for i in range(2, end + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for want in wanted:
    print(dp[want][0], dp[want][1])
