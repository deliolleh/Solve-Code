# 입력
number = int(input())
# 각 자릿수의 합
total = 0

while number >= 1:
    # 마지막 자리의 수를 구하기
    plus = number % 10
    total += plus
    # 다음 자릿수를 구하기 위해 마지막 자리 제거
    number //= 10

print(total)