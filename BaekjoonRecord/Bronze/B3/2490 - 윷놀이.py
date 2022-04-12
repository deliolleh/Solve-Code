for i in range(3):
    wu = list(map(int, input().split()))

    if sum(wu) == 3:
        print('A')
    elif sum(wu) == 2:
        print('B')
    elif sum(wu) == 1:
        print('C')
    elif sum(wu) == 0:
        print('D')
    else:
        print('E')
