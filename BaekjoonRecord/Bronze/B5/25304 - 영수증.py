X = int(input())

N = int(input())

res = 0
for _ in range(N):
    money, count = map(int, input().split())
    res += money * count

print("Yes") if X == res else print("No")
