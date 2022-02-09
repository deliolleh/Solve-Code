# 받은 수
N = int(input())

# 반복문이 진행될 때마다 2의 i제곱만큼 출력
for i in range(N+1):
    print(f'{2 ** i}', end=' ')
