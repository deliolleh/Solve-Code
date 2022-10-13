N, M = map(int, input().split())

pay = list(map(int, input().split()))

max_pay = 0

for i in range(N - M):
    total = 0
    for j in range(M):
        total += pay[i + j]

    if total > max_pay:
        max_pay = total

print(max_pay)
