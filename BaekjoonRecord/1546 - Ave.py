Test_case = int(input())
Score = list(map(int, input().split()))
max_score = Score[0]
new_ave = 0

for i in Score:
    if max_score < i:
        max_score = i

for i in range(len(Score)):
    Score[i] = Score[i] / max_score * 100

for i in Score:
    new_ave = new_ave + i

print(new_ave/len(Score))