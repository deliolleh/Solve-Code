music = list(map(int, input().split()))
# 마주한 값 차이가 |1|일 때만 등록, 나머지는 0으로 초기화하고 break
gap = 0

for i in range(0, len(music)-1):
    # 마주한 인덱스 값 사이의 차이 측정
    diff = music[i] - music[i+1]
    # 한번이라도 차이가 1 이상이면 바로 break
    if abs(diff) != 1:
        gap = 0
        break
    # 첫 차이값이 |1|일 때, 이후 값이 다를 경우 break
    elif i != 0 and gap != diff:
        gap = 0
        break
    # gap에 diff 값 등록
    else:
        gap = diff

if gap == -1:
    print('ascending')
elif gap == 1:
    print('descending')
else:
    print('mixed')