a, b = map(int, input().split())

cds = []
gcd = 0

for n in range(1, min(a, b)+1):
    if a % n == 0 and b % n == 0:
        cds.append(n)
        gcd = n

lcm = gcd * (a // gcd) * (b // gcd)

print(gcd, lcm)
