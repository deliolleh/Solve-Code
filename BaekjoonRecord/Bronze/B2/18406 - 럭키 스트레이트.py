sco = input()

a = sum(list(map(int, sco[: len(sco) // 2])))
b = sum(list(map(int, sco[len(sco) // 2 :])))

if a == b:
    print("LUCKY")
else:
    print("READY")
