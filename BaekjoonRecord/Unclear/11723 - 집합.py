import sys

ex = [0] * 21

for tc in range(int(input())):
    order = list(sys.stdin.readline().split())

    if order[0] == 'add':
        ex[int(order[1])] = 1

    elif order[0] == 'remove' and order[1] in ex:
        ex[int(order[1])] = 0

    elif order[0] == 'check':
        print(ex[int(order[1])])

    elif order[0] == 'toggle':
        ex[int(order[1])] = abs(ex[int(order[1])] - 1)

    elif order[0] == 'all':
        ex = [1] * 21

    else:
        ex = [0] * 21
