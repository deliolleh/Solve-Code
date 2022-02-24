TC = int(input())

for tc in range(1, TC+1):
    length = int(input())

    arr = list(input().split())
    if length % 2 == 1:
        A = arr[:length//2+1]
        B = arr[length//2+1:]
    else:
        A = arr[:length//2]
        B = arr[length//2:]

    for i in range(len(A)):
        arr[2*i] = A[i]
    for j in range(len(B)):
        arr[1+2*j] = B[j]

    print(f'#{tc}', end=' ')
    print(*arr)
