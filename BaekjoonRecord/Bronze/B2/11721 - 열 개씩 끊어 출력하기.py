income = input()

while True:
    print(income[:10])
    income = income[10:]

    if len(income) <= 10:
        print(income)
        break