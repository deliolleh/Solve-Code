N, K = map(int, input().split())

values = []
for n in range(N):
    values.append(int(input()))

count = 0
for value in values[-1: :-1]:
    if K >= value:
        count += K // value
        K = K % value

    if K < values[0]:
        break

print(count)
