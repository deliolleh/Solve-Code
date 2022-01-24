# 테스트 케이스 수 T
T = int(input())

for i in range(1,T+1):
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num

    print(f'#{i} {max_num}')