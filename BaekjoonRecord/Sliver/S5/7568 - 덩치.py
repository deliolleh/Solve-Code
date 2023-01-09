import sys

N = int(input())

people = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append([weight, height])

compare = [1] * N

for index in range(N):
    for index2 in range(N):
        if people[index][0] < people[index2][0] and people[index][1] < people[index2][1]:
            compare[index] += 1

print(" ".join(list(map(str, compare))))
