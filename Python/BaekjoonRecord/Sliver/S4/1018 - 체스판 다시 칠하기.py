col, row = map(int, input().split())

board = []

for index in range(col):
    board.append(input())

min_change = int(10e9)
min_change_reverse = int(10e9)

for i in range(col - 7):
    for j in range(row - 7):
        now_change = 0
        now_change_reverse = 0
        for i2 in range(8):
            for j2 in range(8):
                if ((i2 + j2) % 2 == 0 and board[i + i2][j + j2] == "B") or (
                        (i2 + j2) % 2 and board[i + i2][j + j2] == "W"):
                    now_change += 1
                if ((i2 + j2) % 2 == 0 and board[i + i2][j + j2] == "W") or (
                        (i2 + j2) % 2 and board[i + i2][j + j2] == "B"):
                    now_change_reverse += 1

        min_change = min(min_change, now_change, now_change_reverse)

print(min_change)


# col, row = map(int, input().split())
#
# board = []
#
# for index in range(col):
#     board.append(input())
#
# min_change = int(10e9)
#
# for i in range(col - 7):
#     for j in range(row - 7):
#         now_change_white = 0
#         now_change_black = 0
#         for i2 in range(8):
#             for j2 in range(8):
#                 if (i2 + j2 % 2 == 0 and board[i + i2][j + j2] != "W") or (i2 + j2 % 2 and board[i + i2][j + j2] != "B"):
#                     now_change_white += 1
#                 if (i2 + j2 % 2 == 0 and board[i + i2][j + j2] != "B") or (i2 + j2 % 2 and board[i + i2][j + j2] != "W"):
#                     now_change_black += 1
#
#         min_change = min(min_change, now_change_white, now_change_black)
#
# print(min_change)
