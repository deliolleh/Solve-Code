import sys

# 수의 개수 N
N = int(input())

# 중복을 허용하기 않으므로 빈 셋 할당
num_set = set()

for i in range(N):
    num_set.add(int(sys.stdin.readline()))

num_list = sorted(list(num_set))

for num in num_list:
    print(num)
