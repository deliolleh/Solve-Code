# 1
A, B, C = map(int, input().split())
print(f'{(A + B) % C}\n{((A % C) + (B % C)) % C}\n{(A * B) % C}\n{((A % C) * (B % C)) % C}')

# 2
A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
