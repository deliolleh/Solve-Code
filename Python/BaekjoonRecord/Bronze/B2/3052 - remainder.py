B = []

for i in range(0, 10):
    A = int(input())
    B.append(A % 42)

C = set(B)

B = list(C)

print(len(B))
