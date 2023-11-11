K = int(input())

# 확정 리스트, 확인 변수
result = []
check = 0

for i in range(K):
    check = int(input())
    if check != 0:
        result.append(check)

    else:
        if i > 0:
            result.pop()
        else:
            continue

if len(result) == 0:
    print(0)
else:
    print(sum(result))
