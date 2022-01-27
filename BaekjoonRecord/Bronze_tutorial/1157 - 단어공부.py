# 입력받는 값을 list형태로 받음
Sen = list(input())
# 알파벳 수만큼 리스트를 만듦
alp_list = [0]*26

# 단어에서 가장 많이 쓴 알파벳 측정
for let in Sen:
    # 문자를 아스키코드로 변환
    o_let = ord(let)
    # let이 대문자일 경우
    if 64 < o_let < 91:
        alp_list[o_let - 65] += 1
    # let이 소문자일 경우
    if 96 < o_let < 123:
        alp_list[o_let - 97] += 1

# 쓰지 않은 인덱스 삭제
alt_alp_list = sorted(alp_list, reverse=True)
i = 0
while True:
    try:
        if alt_alp_list[i] == 0:
            del alt_alp_list[i]
            i += 1
    except KeyboardInterrupt:
        break

# 같은 횟수인 알파벳이 존재하는지 확인
most_use = 0
overlap = 0
most_use_index = alt_alp_list[0]
for i in range(len(alt_alp_list)):
    if most_use_index < alt_alp_list[i]:
        most_use_index = alt_alp_list[i]
        most_use = i
    elif most_use_index == alt_alp_list[i]:
        overlap = 1
        break
    else:
        pass

if overlap == 1:
    print('?')
else:
    print(chr(most_use_index + 65))

# Wrong