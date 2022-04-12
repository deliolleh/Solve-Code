# 테스트 케이스 수
T = int(input())


def n_room(height, width, number):
    n = 1
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            if n == number:
                if 0 < w < 10:
                    return str(h) + '0' + str(w)
                else:
                    return str(h) + str(w)
            n += 1


for t in range(T):
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    H, W, N = map(int, input().split())

    print(n_room(H, W, N))

    # # (idx+1)번째 손님이 들어간 방을 표시하는 리스트
    # customer_room = []
    # # (n+1)번째 손님
    # n = 0
    # # N번쨰 손님이 오면 1로 변환
    # flag = 0
    #
    # for w in range(1, W+1):
    #     if flag == 1:
    #         print(customer_room[N - 1])
    #         break
    #     for h in range(1, H+1):
    #         if n == N:
    #             flag = 1
    #             break
    #         if 0 < w < 10:
    #             customer_room.append(str(h)+'0'+str(w))
    #         else:
    #             customer_room.append(str(h) + str(w))
    #         n += 1
