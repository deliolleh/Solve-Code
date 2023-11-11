for tc in range(1, int(input()) + 1):
    print(f'#{tc}')
    # 받을 줄의 수
    N = int(input())
    # 입력받을 문자를 담을 변수
    ten = ''

    for i in range(N):
        # 넣을 단어, 넣는 횟수
        a, b = input().split()
        b = int(b)
        # b만큼 a를 반복해서 입력
        for j in range(b):
            ten += a
            # 길이가 10이 되면
            # 출력하고 초기화
            if len(ten) == 10:
                print(ten)
                ten = ''

    # 마지막에 10 이하의 글자가 담겨있으면
    # 이를 출력
    if len(ten) != 0:
        print(ten)
