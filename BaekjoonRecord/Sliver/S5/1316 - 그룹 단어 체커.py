TC = int(input())

not_group = 0

for tc in range(TC):
    letter = input()

    letter_list = []
    for idx in range(len(letter)):
        if letter[idx] in letter_list and letter[idx] != letter[idx - 1]:
            not_group += 1
            break
        else:
            letter_list.append(letter[idx])

print(TC - not_group)
