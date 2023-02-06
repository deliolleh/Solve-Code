start = int(input())

# 처음에는 DFS 방식을 생각했으나 어김없이 시간초과가 났다
# 결국 알고리즘 분류를 보고 Dynamic Programming인 것을 확인
# bottom-up 구조를 위한 Array 생성
dp = [0] * (start + 1)

# 여기서 99% 오답이 나왔다
# 범위가 1 <= x <= 10 ** 6
# 범위가 1인 경우에 대해 처리를 해줘야한다
if start > 1:
    dp[2] = 1

# 처음에 문제를 잘못 읽어 위에서부터 조건 만족하면 그것만 한다는 걸로 잘못 봤었음
# 다시 읽어보니 다 해야했다
# 1. a 3의 배수면 3으로 나눈다
# 2. b 2의 배수(짝수)면 2로 나눈다
# 3. c 1을 뺀다
# 위의 방식으로 다음 수를 계산하면 a, b, c는 무조건 지금 num보다 작기 때문에
# bottom-up 구조 상 이미 계산하고 간 숫자들이다
# 그래서 해당 숫자들이 필요한 횟수에 1를 더한다
# 그렇게 구한 count1, count2, count3 중 가장 작은 것이 dp[num]의 값이 된다
# 이 때 count들의 초기값은 min을 구해야함으로 큰 수를 입력해야한다
# (처음에 깜빡하고 0 처리함)
for num in range(3, start + 1):
    count1, count2, count3 = 10 ** 7, 10 ** 7, 10 ** 7
    if num % 3 == 0:
        num1 = num // 3
        count1 = 1 + dp[num1]

    if num % 2 == 0:
        num2 = num // 2
        count2 = 1 + dp[num2]

    num3 = num - 1
    count3 = 1 + dp[num3]
    dp[num] = min(count1, count2, count3)

# 모든 수를 구하고 나면 가장 마지막 index가 start의 값이므로 이를 출력
print(dp[-1])