import sys

while True:
    line = sys.stdin.readline().rstrip()
    if len(line) == 1:
        break

    balance = []
    for li in line:
        if li == "(" or li == ")" or li == "[" or li == "]":
            balance.append(li)

    while True:
        if len(balance) <= 1:
            if len(balance) == 0:
                print("yes")
            else:
                print("no")
            break

        state = 1
        for idx in range(len(balance) - 1):
            if balance[idx] == "(" and balance[idx + 1] == ")":
                balance = balance[:idx] + balance[idx + 2 :]
                state = 0
                break
            elif balance[idx] == "[" and balance[idx + 1] == "]":
                balance = balance[:idx] + balance[idx + 2 :]
                state = 0
                break

        if state == 1:
            print("no")
            break
