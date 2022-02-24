import sys


# 받은 길이 n의 a를 정렬할 때 정렬 횟수가 k인 것을 찾는 함수
def selection_sort_kth(a, n, k):
    # 변수 초기화
    cnt = 0
    # 예시에는 1~N => 인덱스 기준 0 ~ n-1
    # 2 to N => 1 ~ N-1 => range(1, n)
    for idx1 in range(1, n):
        # 마지막에 가장 작은 값이 들어올 곳
        loc = idx1 - 1
        # 마지막에 loc에 들어갈 값을 받는 변수
        new_item = a[idx1]

        # [0:idx1-1]까지는 정렬된 상태 => loc = 0 에선 통과
        while 0 <= loc and new_item < a[loc]:
            a[loc + 1] = a[loc]
            loc -= 1
            cnt += 1
            if cnt == k:
                return a

        # 값 교환
        if loc + 1 != idx1:
            a[loc + 1] = new_item
            cnt += 1

        if cnt == k:
            return a

    return [-1]


N, K = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))

print(*selection_sort_kth(arr, N, K))
