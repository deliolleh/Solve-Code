from collections import deque
import sys

for tc in range(int(input())):
    p = list(sys.stdin.readline().rstrip())
    flag = 0

    N = int(input())
    arr = list(input())
    arr = arr[1:len(arr) - 1]
    if p.count('D') < len(arr):
        arr = list(map(int, ''.join(arr).split(',')))
        arr = deque(arr)

        for order in p:
            try:
                if order == 'R':
                    arr.reverse()
                elif order == 'D' and len(arr):
                    arr.popleft()
                else:
                    flag = 1
                    break
            except:
                flag = 1
                break
    else:
        flag = 1

    if flag:
        print('error')
    else:
        print(list(arr))
