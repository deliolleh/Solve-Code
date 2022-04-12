alphabet = input()

count = len(alphabet)

for idx in range(len(alphabet)):
    if alphabet[idx] == 'c' or alphabet[idx] == 'd' or alphabet[idx] == 'l' or alphabet[idx] == 'n' or alphabet[
        idx] == 's' or alphabet[idx] == 'z':
        if alphabet[idx:idx + 2] == 'c=' or alphabet[idx:idx + 2] == 'c-' or alphabet[idx:idx + 3] == 'dz=' or alphabet[
                                                                                                               idx:idx + 2] == 'd-':
            count -= 1
        elif alphabet[idx:idx + 2] == 'lj' or alphabet[idx:idx + 2] == 'nj' or alphabet[
                                                                               idx:idx + 2] == 's=' or alphabet[
                                                                                                       idx:idx + 2] == 'z=':
            count -= 1

print(count)
