# A가 0이 되면 루프를 꺼주는 시스템 변수 기입
sys = 1

while sys>0:
    A,B = map(int, input().split())
    if A > 0:
        C = A + B
        print(C)

    if A == 0:
        sys = 0
