# i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체의 갯수
def f(i, n, k):
    # 한 개의 부분집합 완성
    if i == n:
        s = 0
        for j in range(n):
            if bit[j]:
                s += a[j]
                # print(a[j], end=' ')
        # print(f'sum = {s}')

        # 합이 찾는 값과 같다면
        if s == k:
            for j in range(n):
                if bit[j]:
                    print(a[j], end=' ')
            print()

    else:
        bit[i] = 1
        f(i + 1, n, k)
        bit[i] = 0
        f(i + 1, n, k)


a = [1, 2, 3]
bit = [0, 0, 0]
K = 3
f(0, 3, 3)
