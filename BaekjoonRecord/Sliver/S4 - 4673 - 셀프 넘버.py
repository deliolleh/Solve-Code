num = 1
have_self = set()
while num < 10000:
    line = 0
    for n in str(num):
        line += int(n)

    self_num = num + line

    have_self.add(self_num)

    num += 1

num_set = set()
for n in range(1, 10001):
    num_set.add(n)

result = list(num_set - have_self)
result.sort()

for i in result:
    print(i)
