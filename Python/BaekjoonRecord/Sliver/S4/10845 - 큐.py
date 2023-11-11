import sys

# Test Case
N = int(input())

# Stack
stack = []

for n in range(N):
    order = sys.stdin.readline()
    length = len(stack)

    if "us" in order:
        stack.append(int(order[5:]))

    elif "po" in order:
        try:
            print(stack.pop(0))
        except:
            print(-1)

    elif "si" in order:
        print(len(stack))

    elif "em" in order:
        if length > 0:
            print(0)
        else:
            print(1)

    else:
        try:
            if "fr" in order:
                print(stack[0])
            else:
                print(stack[-1])
        except:
            print(-1)
