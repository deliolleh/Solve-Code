import sys


# 받은 길이 n의 a를 정렬할 때 정렬 횟수가 k인 것을 찾는 함수
def bubble_sort_kth(a, n, k):
    # 변수 초기화
    cnt = 0
    # 일반적인 버블 정렬 방법
    for idx1 in range(n - 1, 0, -1):
        for idx2 in range(idx1):
            if a[idx2] > a[idx2 + 1]:
                a[idx2], a[idx2 + 1] = a[idx2 + 1], a[idx2]
                # 위치가 변경이 발생하면 cnt + 1
                cnt += 1

            # 전체 반복횟수가 k보다 많으면 cnt가 k와 동일한 시기가 나타남
            # 이 때의 배열 리턴
            if cnt == k:
                return a

    # 전체를 돌았는데 없다는 것은 k가 전체 횟수보다 많음
    # *bubble_sort_kth를 했으므로 에러 방지를 위해 리스트 형태로 출력
    return [-1]


N, K = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))

print(*bubble_sort_kth(arr, N, K))
