N = int(input())

default = N

i = 1

while True:
    c = ((N // 10) + (N % 10)) % 10
    N = ((N % 10) * 10) + c
    if default == N:
        print(i)
        break
    i += 1
