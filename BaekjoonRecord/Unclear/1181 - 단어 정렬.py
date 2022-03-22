letter = set()
N = int(input())
for i in range(N):
    letter.add(input())

list_let = list(letter)

list_let.sort(key=lambda x: (len(x), x[0], x[1]))

for a in list_let:
    print(a)
