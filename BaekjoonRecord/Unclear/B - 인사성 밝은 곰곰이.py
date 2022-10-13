N = int(input())
already = []

cnt = 0
while N > 0:
    mess = input()
    if mess == 'ENTER':
        already.clear()
    elif mess not in already:
        already.append(mess)
        cnt += 1
    N -= 1

print(cnt)
