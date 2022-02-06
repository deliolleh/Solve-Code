N = input()
count = 0

for i in range(len(N)-1, 1, -1):
    if N[i] == 0:
        count += 1
    else:
        break

print(count)
