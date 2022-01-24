# 테스트 케이스 수
T = int(input())

# 테스트 케이스 수만큼 반복
for i in range(1,T+1):
    # 두 수 입력 받기
    A, B = input().split()

    # 출력
    print(f'#{i} {int(A)// int(B)} {int(A)%int(B)}')