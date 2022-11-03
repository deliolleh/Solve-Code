# input MBTI
mbti = input()

total = [["I", "E"], ["S", "N"], ["T", "F"], ["P", "J"]]
result = []

for idx in range(len(mbti)):
    total[idx].remove(mbti[idx])
    result.extend(total[idx])

# for one in result:
#     print(one, end='')

print("".join(result))
