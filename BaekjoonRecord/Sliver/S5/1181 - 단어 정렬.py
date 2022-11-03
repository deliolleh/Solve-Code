N = int(input())

arr = list()

for n in range(N):
    arr.append(input())

arr = list(set(arr))

# sort 연습할만한 조건
arr.sort(key=lambda x: (len(x), x))

print(*arr, sep="\n")
