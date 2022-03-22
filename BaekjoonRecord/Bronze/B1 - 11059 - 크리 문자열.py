num = input()
max_len = 0
for l in range(2, len(num)+1, 2):
    for i in range(0, len(num) - l + 1):
        if sum(list(map(int, num[i: i + l // 2]))) == sum(list(map(int, num[i + l // 2: i + l]))):
            if l > max_len:
                max_len = l

print(max_len)
