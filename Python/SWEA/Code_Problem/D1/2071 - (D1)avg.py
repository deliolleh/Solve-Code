# 테스트 케이스 수 받기
test_case = int(input())

for i in range(0, test_case):
    # 총합 초기화
    total = 0

    # 테스트 케이스 받기
    list_num = list(map(int, input().split()))

    # 케이스 내부 값을 전부 더하기
    for num in list_num:
        total += num

    # 평균값 구하기
    list_avg = round(total / 10)
    print(f'#{i+1} {list_avg}')