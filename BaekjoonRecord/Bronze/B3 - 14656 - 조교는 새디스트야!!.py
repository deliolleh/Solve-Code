N = int(input())

students = list(map(int, input().split()))

hurt = 0
for idx in range(N):
    if students[idx] != idx+1:
        hurt += 1

print(hurt)