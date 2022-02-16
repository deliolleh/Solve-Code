import sys

num = sys.stdin.readline().strip()

dec = 0
for idx in range(len(num)):
    dec += int(num[idx]) * 8 ** (len(num) - idx - 1)

bit = []
while True:
    bit.append(str(dec % 2))
    dec //= 2
    if dec == 1:
        bit.append('1')
        break

print(''.join(bit.reverse()))
