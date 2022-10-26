# Condition
k, n = map(int, input().split())
cables = []
possible = 0

# get input to list cable
for ca in range(k):
    cable = int(input())
    cables.append(cable)
    if cable > possible:
        possible = cable

start = 1
end = possible

long = 0
while start <= end:
    mid = (start + end) // 2
    make = sum(list(map(lambda x: x // mid, cables)))
    if make >= n:
        start = mid + 1
        long = max(long, mid)

    else:
        end = mid - 1

print(long)