# Test Case
N = int(input())

for i in range(1, N+1):
    num = list(map(int, input().split()))

    max_count = num.count(max(num))
    min_count = num.count(min(num))
    num.sort()

    num = num[min_count: len(num)-max_count]

    print(f'#{i} {sum(num)/len(num):.0f}')
