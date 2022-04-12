N, K = map(int, input().split())

# 1 ~ N번
stack = [i for i in range(1, N + 1)]
# 1번의 idx가 0부터이므로 이를 맞추기 위해 -1에서 시작
cnt = -1
res = []
# 아무도 없을 때까지
while len(stack) != 0:
    length = len(stack)
    # -1 + K에는 K번 사람이 있음
    cnt += K
    # length가 계속 변하므로 while문 사용
    if cnt >= length:
        cnt %= length
    # 현재 cnt가 위치한 idx의 사람을 제거하고 res에 추가
    res.append(stack.pop(cnt))
    # 제거된 자리로 원래 cnt + 1 idx의 수가 내려오므로
    # 이를 맞추기 위해 1을 뺌
    cnt -= 1

print('<', end='')
for idx in range(N):
    if idx != N - 1:
        print(res[idx], end=', ')
    else:
        print(f'{res[idx]}>')
