# 테스트케이스 수 받기
N = int(input())

# 테스트 케이스 받기
num_list = list(map(int, input().split()))

# 케이스의 길이 측정
length = len(num_list)

# 리스트 N번쨰 값을 기준으로 N미만의 M번째 값을 비교해 함수정렬
for idx in range(1, length):
    for idx2 in range(idx):
        if num_list[idx2] > num_list[idx]:
            tem = num_list[idx2]
            num_list[idx2] = num_list[idx]
            num_list[idx] = tem

# 길이의 절반인 length/2 인덱스의 값을 출력
print(num_list[(length//2)])