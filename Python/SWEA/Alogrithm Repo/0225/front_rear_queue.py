# 가장 느림

import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

while q:
    print(q.get())