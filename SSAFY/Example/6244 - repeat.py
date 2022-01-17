list_score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

while len(list_score):
    i = list_score.pop()
    if i >= 80:
        total += i

print(total)