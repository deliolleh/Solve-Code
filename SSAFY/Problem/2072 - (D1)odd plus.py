# 테스트 케이스 수 받기
test_case = int(input())

for i in range(0, test_case):
    # total 초기화
    total = 0

    # 테스트 케이스 입력
    list_num = list(map(int, input().split()))

    # 홀수만 total에 더하기
    for num in list_num:
        if num % 2:
            total += num
    print(f'#{i+1} {total}')