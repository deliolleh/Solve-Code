for tc in range(1, int(input()) + 1):
    N = int(input())
    num = []
    # i * N에서 i를 담당
    i = 1

    while True:
        # 새로운 양 입장
        now = i * N
        check = str(now)

        # check에 있는 숫자들이 num에 없으면 추가
        for n in check:
            if int(n) not in num:
                num.append(int(n))

        # 0 ~ 9까지 10개가 다 채워지면 그 순간의 now 출력하고 break
        if len(num) == 10:
            print(f'#{tc} {now}')
            break

        i += 1
