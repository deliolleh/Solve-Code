import heapq

# 최소 힙
# heap = [7, 2, 5, 3, 4, 6]
# heapq.heapify(heap)
# print(heap)
# heapq.heappush(heap, 1)
# print(heap)
# while heap:
#     print(heapq.heappop(heap), end=' ')

heap = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(heap)):
    heapq.heappush(heap2, -heap[i])
print(*list(map(lambda x: -x, heap2)))
