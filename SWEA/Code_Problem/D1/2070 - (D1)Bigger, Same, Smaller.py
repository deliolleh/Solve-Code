# 테스트 케이스 수 T
T = int(input())

# 각 케이스 별 부호 결정
for i in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        state = '>'
    elif a < b:
        state = '<'
    else:
        state = '='

    # 출력
    print(f'#{i} {state}')
