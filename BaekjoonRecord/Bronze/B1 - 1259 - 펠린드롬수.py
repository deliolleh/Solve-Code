while True:
    flag = 0
    int_p = int(input())

    if int_p == 0:
        break

    else:
        num_s = str(int_p)
        num = []

        for n in num_s:
            num.append(n)

        if len(num) == 3:
            for i in range(1):
                if num[i] != num[-1]:
                    flag = 1

        else:
            for i in range(len(num)//2):
                if num[i] != num[-1-i]:
                    flag = 1

        if flag == 0:
            print('yes')
        else:
            print('no')