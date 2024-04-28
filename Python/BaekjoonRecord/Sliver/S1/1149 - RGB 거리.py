# DP로 푸는 문제

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[10 ** 9] * 3 for _ in range(N)]

# 첫 번째 집을 빨, 초, 파로 칠했을 때를 dp의 0번째 경우의 수
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

# i번째 집은 i-1, i+1 번째 집과 색이 달라야 함으로
# i번째 에서 현재 본인의 row 값과 다른 값 중 작은 값과 이번 값을 더한다
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

# 마지막 N번 계산 후 dp의 마지막 index 의 최소 값을 가져 온다
print(min(dp[N - 1]))
