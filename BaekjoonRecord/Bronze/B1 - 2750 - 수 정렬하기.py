N = int(input())

# sort 사용하지 않고 풀기
result = []
for n in range(N):
    result = [int(input())] + result

    # 리스트 길이가 2 이상일 때 교환이 가능
    if len(result) > 1:
        for idx in range(len(result)-1):
            if result[idx] > result[idx+1]:
                result[idx], result[idx+1] = result[idx+1], result[idx]

for res in result:
    print(res)
