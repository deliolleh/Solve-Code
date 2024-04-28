def dif(x):
    return x ** 2 - (x-1) ** 2

before = 0
before_gap = 0

i = 2
while i < 10 ** 4:
    now = dif(i)
    if before != 0:
        now_gap = now - before
        if before_gap != 0:
            if now_gap - before_gap != 2:
                print("get difference ", now)
                break
            before_gap = now_gap

    before = now
    i += 1

print("DONE")