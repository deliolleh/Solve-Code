# 카드의 개수와 Max의 수
N, M = map(int, input().split())

# 세 카드 합을 입력받을 변수
max_sum = 0

# 카드들을 입력받을 리스트
card = list(map(int, input().split()))

# n, n2, n3가 모두 다를 때 세 카드 합이 M을 넘지 않고 기존 max_sum 값을 가질 때, max_sum을 갱신함
for n in range(N):
    for n2 in range(N):
        for n3 in range(N):
            if n != n2 and n != n3 and n2 != n3:
                plus = card[n] + card[n2] + card[n3]
                if M >= plus > max_sum:
                    max_sum = plus

print(max_sum)
