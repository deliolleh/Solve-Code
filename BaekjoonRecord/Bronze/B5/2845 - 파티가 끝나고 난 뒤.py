L, P = map(int, input().split())
news = list(map(int, input().split()))

total = L * P

ans = []
for new in news:
    ans.append(new - total)

print(*ans)
