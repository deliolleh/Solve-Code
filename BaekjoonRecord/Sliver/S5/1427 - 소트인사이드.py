num = input()

num_list = list()
for i in range(len(num)):
    num_list.append(num[i])

num_list.sort(reverse=True)
print(''.join(num_list))