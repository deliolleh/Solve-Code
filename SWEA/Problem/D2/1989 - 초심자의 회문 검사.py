# 테스트 케이스 수
T = int(input())

# 케이스 별 작동
for t in range(1, T+1):
    # 입력받은 문자 입력
    case = input()

    # 결과값을 받을 변수 입력
    output = 1

    # 받은 문자들은 iterable하기에 반복문이 가능
    # 이 때 범위를 문자 길이를 2로 나누었을 때의 몫으로 한다.
    # (x.5 경우가 나왔을 때 x까지만 하도록)
    for idx in range(len(case)//2):
        if case[idx] != case[-1-idx]:
            output = 0
            break
        else:
            pass

    # output 값에 따라 결과 출력
    print(f'#{t} {output}')
