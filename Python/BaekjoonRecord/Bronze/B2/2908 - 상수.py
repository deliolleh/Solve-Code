# 두 수 입력 받기
A, B = map(int, input().split())


def reverse_num(num):
    # 수를 뒤집는 함수 생성
    num_100 = num // 100
    num_10 = (num // 10) % 10
    num_1 = num % 10
    return num_1 * 100 + num_10 * 10 + num_100


if reverse_num(A) > reverse_num(B):
    # 바꾼 값을 비교
    print(reverse_num(A))
else:
    print(reverse_num(B))
