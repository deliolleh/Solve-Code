import random

f = open("eval_input.txt", 'w')

for time in range(50):
    cnt = random.randrange(1, 100)
    refill = random.randrange(1, 100)
    X = random.randrange(1, 100)
    Y = random.randrange(1, 100)
    f.write(str(cnt) + ' ')
    f.write(str(refill) + ' ')
    f.write(str(X) + ' ')
    f.write(str(Y) + '\n')

    for i in range(Y):
        inner = list(map(str, range(1, 101)))

        random.shuffle(inner)

        f.write(' '.join(inner[:X]) + '\n')

f.close()
