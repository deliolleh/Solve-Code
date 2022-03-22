for tc in range(1, int(input())+1):
    com = input()
    if len(com) < 15:
        com += 'o' * (15-len(com))

    if com.count('o') > com.count('x'):
        res = 'Yes'
    else:
        res = 'No'

    print(f'#{tc} {res}')

