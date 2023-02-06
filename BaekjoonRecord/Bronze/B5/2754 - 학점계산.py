# A+ 4.3 A0 4.0 A- 3.7
# ...

score = input()
result = 0

if score[0] == "A":
    result += 4
elif score[0] == "B":
    result += 3
elif score[0] == "C":
    result += 2
elif score[0] == "D":
    result += 1

if score[0] != "F":
    if score[1] == "+":
        result += 0.3
    elif score[1] == "-":
        result -= 0.3
    else:
        result = str(result) + ".0"
else:
    result = "0.0"

print(result)