for tc in range(1, int(input()) + 1):
    # 두 개의 날짜
    days = list(map(int, input().split()))

    be = days[:2]
    af = days[2:]

    # 두 날짜 간의 차이
    res = 0

    # 각 달의 마지막 날을 딕셔너리 형태로 구성
    month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,
             '12': 31}

    # 앞 날짜 다음날부터 뒷 날짜 전달까지의 날 합
    for i in range(be[0] + 1, af[0]):
        res += month[str(i)]

    # 두 날짜의 달이 다르면 => (앞 달의 총 일 - 앞 날짜의 날) + 뒷 날의 날 + 1(a<=x<=b의 형태이기에)
    if be[0] != af[0]:
        res += (month[str(be[0])] - be[1]) + af[1] + 1
    # 같으면(3월 14/ 3월 21일) => 뒷 날짜 날 - 앞 날짜 날 + 1
    else:
        res += af[1] - be[1] + 1

    print(f'#{tc} {res}')
