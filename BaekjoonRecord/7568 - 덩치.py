import sys

# 전체 사람의 수 N
N = int(sys.stdin.readline())

people_size = []

for i in range(N):
    people_size.append(list(map(int, sys.stdin.readline().split())))

result = []
for person1 in people_size:
    i_m_big = 0
    for person2 in people_size:
        if person1[0] > person2[0] and person1[1] > person2[1]:
            i_m_big += 1
    result.append(i_m_big)

print(result)
