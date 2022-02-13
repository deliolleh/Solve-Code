num = list(map(int, input().split()))

num.sort()

num.pop()

print(num[-1])
