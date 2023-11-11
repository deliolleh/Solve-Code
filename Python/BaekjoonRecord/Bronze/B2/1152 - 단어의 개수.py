# 문장을 받을 변수를 리스트 형태로 받음
Sen = list(input())
# 공백의 수를 셀 변수 입력(최소 1단어가 존재 해야 입력 받음)
cnt = 0

for i in range(len(Sen)):
    if i == 0 and Sen[0] != " ":
        cnt += 1
    elif Sen[i - 1] == " " and Sen[i] != " ":
        cnt += 1
    else:
        pass
        # 단어가 첫 인덱스에 들어있거나, 직전 인덱스에 공백이 들어있으면 증가시킨다.
print(cnt)
