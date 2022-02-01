# 받은 수
N = int(input())

# 총합 받을 변수
total = 0

# While문으로 총합 계산
while True:
    if N <1:
        print(total)
        break
    total += N
    N -= 1
