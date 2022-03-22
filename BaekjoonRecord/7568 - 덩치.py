N = int(input())

peo = [list(map(int, input().split())) for _ in range(N)]
check = [0] * N

for i in range(N):
    for j in range(N):
        if i != j and peo[i][0] > peo[j][0] and peo[i][1] > peo[j][1]:
            check[i] += 1

check_line = sorted(list(set(check)), reverse=True)
res = [0] * N
n = 1
for i in range(len(check_line)):
    for j in range(N):
        if check[j] == check_line[i]:
            res[j] = n

    n += check.count(i)

print(*res)
