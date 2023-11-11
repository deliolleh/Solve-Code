w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

p = p + t
if (p // w) % 2:
    p = w - (p % w)
else:
    p = p % w

q = q + t
if (q // h) % 2:
    q = h - (q % h)
else:
    q = q % h

print(p, q)
