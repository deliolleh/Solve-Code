# For use ceil, call math
import math

# Condition
k, n = map(int, input().split())
cable = []

# get input to list cable
for ca in range(k):
    cable.append(int(input()))

# Calculate for limit range
max_length = math.ceil(min(cable)//(n//k))

# To calculate highest length, start to max_length to 1
for length in range(max_length, 0, -1):
    total = 0
    for ca2 in cable:
        total += ca2 // length

    if total >= n:
        print(length)
        break
