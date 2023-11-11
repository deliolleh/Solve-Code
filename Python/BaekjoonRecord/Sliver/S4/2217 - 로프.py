N = int(input())

loop = []
for _ in range(N):
    loop.append(int(input()))

loop.sort(reverse=True)

# weight = []
# for i in range(N):
#     weight.append(loop[i] * (i + 1))
#
# print(max(weight))

# max_weight = 0
# while loop:
#     now = loop[-1] * len(loop)
#     if now > max_weight:
#         max_weight = now
#     loop.pop()
#
# print(max_weight)