import sys

N = int(input())

stack = []
res = 1

for n in range(N):
    stack.append(int(sys.stdin.readline()))

# 가장 큰 막대기 뒤에 보이지 않으므로 무시
stop = stack.index(max(stack))
#
now_high = stack[-1]

for idx in range(N - 2, stop - 1, -1):
    if stack[idx] > now_high:
        res += 1
        now_high = stack[idx]

print(res)
