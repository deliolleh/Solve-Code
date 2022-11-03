# 한수의 현재 위치 (x,y)/ 직사각형 왼쪽밑 꼭지점(0,0)에서 오른쪽위 꼭지점(w,h)
x, y, w, h = map(int, input().split())

range_list = []

# y축에 평행한 변과의 거리 측정
for xaxis in [0, w]:
    for yaxis in range(h):
        range_list.append(((abs(x - xaxis)) ** 2 + (abs(y - yaxis)) ** 2) ** 0.5)

# x축에 평행한 변과의 거리 측정
for yaxis in [0, h]:
    for xaxis in range(w):
        range_list.append(((abs(x - xaxis)) ** 2 + (abs(y - yaxis)) ** 2) ** 0.5)

# 출력은 정수형으로 출력하도록 한다
print(int(min(range_list)))
