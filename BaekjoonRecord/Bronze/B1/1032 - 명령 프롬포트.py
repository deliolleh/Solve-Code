N = int(input())

first = list(input())

for i in range(N-1):
    ne = list(input())
    for idx in range(len(first)):
        if first[idx] != ne[idx]:
            first[idx] = '?'

print(''.join(first))
