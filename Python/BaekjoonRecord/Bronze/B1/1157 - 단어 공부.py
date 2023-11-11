letter = list(input())

for i in range(len(letter)):
    letter[i] = letter[i].lower()

same = "".join(letter)

one_dict = {}
for one in same:
    if one not in one_dict:
        one_dict[one] = same.count(one)

max_lett = ""
max_let = 0
error_count = 0
for key, value in one_dict.items():
    if max_let < value:
        max_let = value
        max_lett = key
        error_count = 0
    elif max_let == value:
        error_count = 1

if error_count == 1:
    print("?")
else:
    print(max_lett.upper())
