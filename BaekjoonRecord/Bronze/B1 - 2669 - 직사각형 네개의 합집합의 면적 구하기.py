# 평면 초기화
arr = [[0]*100 for _ in range(100)]

# 네 개의 사각형이 x1, y1, x2, y2로 주어짐(x1 < x2, y1 < y2)
for i in range(4):
    sqr = list(map(int, input().split()))
    # arr[col][row]를 좌표 한 점이 아니라 col,row를 왼쪽아래 꼭지점으로 가진
    # 가로1세로1인 단위 사각형이라고 생각하고 1부여
    for row in range(sqr[0], sqr[2]):
        for col in range(sqr[1], sqr[3]):
            arr[col][row] += 1
            # arr[col][row] = 1

# 그대로보면 y=0이 위에 있으므로 확인을 위해
# arr를 뒤집어서 확인
# for a in arr[-1::-1]:
#     print(*a)

# 넓이 초기화
area = 0
# 숫자가 있는 곳 => 네모가 존재하는 곳
# 1씩 증가 => 중복 계산 X
for col in range(100):
    for row in range(100):
        if arr[col][row] != 0:
            area += 1

print(area)
