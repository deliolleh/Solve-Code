# 입력받은 수
N = int(input())

# 5kg, 3kg 봉지가 사용할 수 있는 최대 수량
x, y = (N // 5, N // 3)

# 결과값 입력
z = -1

# 최적의 봉투 수 계산
for i in range(x + 1):
    for j in range(y + 1):
        if 5 * i + 3 * j == N:
            z = i + j

print(z)
