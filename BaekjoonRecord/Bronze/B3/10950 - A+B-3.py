A = int(input())  # input은 무조건 문자열로 받기 때문에 정수화 하기 위해 int

for i in range(1, A + 1):
    B, C = map(int, input().split())
    D = B + C
    print(D)
