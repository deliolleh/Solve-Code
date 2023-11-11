Line = input()

list_Line = list(Line)

for i in range(len(list_Line)):
    o_one = ord(list_Line[i])
    if 96 < o_one <123:
        o_one -= 32
    list_Line[i] = chr(o_one)

print(''.join(list_Line))