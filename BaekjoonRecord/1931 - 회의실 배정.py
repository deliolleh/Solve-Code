N = int(input())

conference = []
for n in range(N):
    conference.append(list(map(int, input().split())))


conference.sort(key=lambda x: (x[1], x[0]))
i = 1
while i < len(conference):
    if conference[i - 1][1] > conference[i][0]:
        conference.pop(i)

    else:
        i += 1

print(len(conference))
