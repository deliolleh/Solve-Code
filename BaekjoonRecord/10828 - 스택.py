import sys
# 명령의 수
N = int(sys.stdin.readline())
# 스택은 순서가 있으므로 가장 유사한 리스트 활용
stack = []
# 명령을 입력받는 변수


def top():
    # top: 가장 마지막에 들어온 스택 출력, 스택이 비었을 때 정수 -1 출력
    if len(stack) != 0:
        print(stack[-1])
    else:
        print('-1')


def empty():
    # empty: 스택이 비어 있으면 1, 아니면 0 출력
    if len(stack) == 0:
        print('1')
    else:
        print('0')


def size():
    # size: 스택의 len 출력
    print(len(stack))


def pop():
    # pop: 스택의 마지막 값을 출력한다. 스택이 비어있으면 -1 출력
    if len(stack) != 0:
        print(stack.pop())
    else:
        print(-1)


def push(x):
    # push X: 스택에 X를 추가(Stack)
    stack.append(x)


for i in range(N):
    order = input().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    else:
        top()

# 시간초과