for tc in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    # 최대/최소 값 받을 변수
    max_num = nums[0]
    min_num = nums[0]
    # 총합
    total = 0

    for num in nums:
        # 최대값 갱신
        if num > max_num:
            max_num = num
        # 최솟값 갱신
        elif num < min_num:
            min_num = num

        total += num

    # 최대 최솟값 빼고
    total -= (max_num + min_num)
    # 길이도 2 뺀다
    length = len(nums) - 2

    # 소수점 첫번째 자리에서 반올림 => .0f 소수점 첫 자리에서 반올림
    # Google is GOD
    print(f'#{tc} {total/length:.0f}')

# 이전 방식
# 뭔가 시간 복잡도가 높은거 같아서 위 방식으로 다시 풀어봄
# Test Case
N = int(input())

for i in range(1, N+1):
    num = list(map(int, input().split()))

    # 최대값 인덱스 측정
    max_count = num.count(max(num))
    # 최솟값 인덱스 측정
    min_count = num.count(min(num))
    # 정렬
    num.sort()

    # 사실상 인덱스 0과 len(num)-1 제거
    num = num[min_count: len(num)-max_count]

    # 인쇄
    print(f'#{i} {sum(num)/len(num):.0f}')