# Num of people
N = int(input())

peo_list = []

for i in range(N):
    age_raw, name = input().split()
    age = int(age_raw)
    peo_list.append([age, i, name])

peo_list_sort = sorted(peo_list, key=lambda x: (x[0], x[1]))

for peo in peo_list_sort:
    print(peo[0], peo[2])
