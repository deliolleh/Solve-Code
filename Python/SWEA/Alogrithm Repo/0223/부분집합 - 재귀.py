# n: 원소의 길이, k: depth
def powerset(n, k):
    global cnt
    cnt += 1
    # 기본파트
    if n == k:
        total = 0
        for i in range(n):
            if bit[i]:
                total += arr[i]

        if total == 10:
            for i in range(n):
                if bit[i]:
                    print(arr[i], end=' ')
            print()

    # 유도파트
    else:
        # k번 요소를 포함
        bit[k] = 1
        powerset(n, k + 1)
        # k번 포함 X
        bit[k] = 0
        powerset(n, k + 1)


arr = list(range(1, 11))
N = len(arr)
bit = [0] * N
cnt = 0
powerset(N, 0)
print(cnt)
