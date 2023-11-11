N = int(input())

y, x = 1, 1
i = 1

phase = True
while i < N:
    if phase:
        my = y - 1
        if N - i >= my:
            i += my
            x, y = x + my, 1
            if i < N:
                i += 1
                x += 1
        else:
            x, y = x + (N - i), y - (N - i)
            i = N
    else:
        mx = x - 1
        if N - i >= mx:
            i += mx
            x, y = 1, y + mx
            if i < N:
                i += 1
                y += 1
        else:
            x, y = x - (N - i), y + (N - i)
            i = N
    phase = not phase

print(f'{y}/{x}')