N = int(input())

letter = input()

total = 0
for n in range(len(letter)):
    total += (ord(letter[n]) - 96) * (31**n)

print(total % 1234567891)
