# 테스트 케이서
T = int(input())

for i in range(T):
    data = []
    data.extend(input())

    vsp_gauge = 0

    while True:
        if len(data) == 0:
            if vsp_gauge == 0:
                print("YES")
            else:
                print("NO")
            break
        now = data.pop()
        if now == ")":
            vsp_gauge += 1
        else:
            vsp_gauge -= 1
            if vsp_gauge < 0:
                print("NO")
                break
