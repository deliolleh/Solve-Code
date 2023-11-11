def sub_set(now, total, lst):
    global cnt
    if now == N:
        if total == S and len(lst) > 0:
            cnt += 1
    else:
        # 이번 원소를 포함
        sub_set(now + 1, total + arr[now], lst + [arr[now]])
        # 이번 원소를 미포함
        sub_set(now + 1, total, lst)


N, S = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
sub_set(0, 0, [])

print(cnt)
