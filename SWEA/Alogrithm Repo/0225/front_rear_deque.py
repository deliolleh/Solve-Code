# deque => double ended queue

from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

while q:
    print(q.popleft())
