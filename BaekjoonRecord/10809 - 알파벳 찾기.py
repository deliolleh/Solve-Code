S = input()
list_alp = [-1]*26

for i in range(len(S)):
    if i > 0 and S[i] == S[i-1]:
        continue
    list_alp[ord(S[i])-97] = i

for i in list_alp[:-1]:
    print(i, end=' ')
print(list_alp[-1])

# Wrong - Find way