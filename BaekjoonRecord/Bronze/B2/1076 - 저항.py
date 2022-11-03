value = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

res = 0
for i in range(3):
    if i == 0:
        res += value.get(input()) * 10
    elif i == 1:
        res += value.get(input())
    else:
        res *= 10 ** value.get(input())

print(res)
