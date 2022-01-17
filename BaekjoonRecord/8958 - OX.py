test_case = int(input())

for i in range(test_case):
    p_p = 0
    score = 0
    result = list(input())
    for res in result:
        if res == 'O':
            score = score + 1 + p_p
            p_p += 1
        else :
            p_p = 0
    print(score)