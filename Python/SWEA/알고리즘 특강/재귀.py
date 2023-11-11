def start(n):
    if n < 6:
        return
    print(n)
    start(n - 1)
    print(n)

start(10)