N = 10
SIZE = N ** 3
q = [0] * SIZE
front = rear = -1

# enQ
rear += 1
q[rear] = 1
rear += 1
q[rear] = 2
rear += 1
q[rear] = 3

while front != rear:
    front += 1
    print(q[front])

print(q)
