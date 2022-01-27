S = input()
# 입력 받은 단어 S
list_alp = [-1]*26
# 알파벳 수 만큼의 빈 리스트 생성

for i in range(len(S)):
    if list_alp[ord(S[i])-97] != -1:
        # 이미 list_alp[i]에서 -1 이외의 값을 가지고 있다면 continue 설정
        continue
    list_alp[ord(S[i])-97] = i

# 입력된 값들을 출력, [-1]에 띄어 쓰기를 막기 위해 따로 출력
for i in list_alp[:-1]:
    print(i, end=' ')
print(list_alp[-1])
