from math import factorial
T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    print(factorial(b) // factorial(b - a) // factorial(a))
