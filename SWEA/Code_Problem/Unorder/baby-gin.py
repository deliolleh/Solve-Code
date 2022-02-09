given = list(map(int, input().split()))

# prof greedy algorithm
num_list = [0] * 12
run_or_triplet = 0

for given in given:
    num_list[given] += 1

for j in range(len(num_list)):
    if num_list[j] >= 3:
        num_list[j] -= 3
        run_or_triplet += 1

    if num_list[j] != 0 and num_list[j+1] != 0 and num_list[j+2] != 0:
        num_list[j] -= 1
        num_list[j+1] -= 1
        num_list[j+2] -= 1
        run_or_triplet += 1

if run_or_triplet == 2:
    print('Bady gin')
else:
    print('Lose')
