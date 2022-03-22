N = int(input())

for n in range(1, N+1):
    letter = list(input().split())
    letter.reverse()
    print(f'Case #{n}:', *letter)
