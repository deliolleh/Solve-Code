max_num = 0
num = 0

for i in range(1, 10):
    new = int(input())
    if max_num < new:
        max_num = new
        num = i

print(max_num)
print(num)
