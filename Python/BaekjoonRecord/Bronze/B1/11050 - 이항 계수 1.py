def fact(num):
    total = 1
    for n in range(1, num + 1):
        total *= n
    return total


A, B = map(int, input().split())

print(int(fact(A) // (fact(B) * fact(A - B))))
