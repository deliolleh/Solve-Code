N = int(input())

sort_list = []
for n in range(N):
    sort_list.append(int(input()))

sort_list.sort()

for one in sort_list:
    print(one)
