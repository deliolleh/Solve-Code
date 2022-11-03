# 못품 => 효율성 불통

# def solution(board, skills):
#     for skill in skills:
#         types, r1, c1, r2, c2, degree = skill
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 if types == 1:
#                     board[r][c] -= degree
#                 else:
#                     board[r][c] += degree
#
#     row = len(board)
#     col = len(board[0])
#     answer = 0
#     for i in range(row):
#         for j in range(col):
#             if board[i][j] > 0:
#                 answer += 1
#
#     return answer


def solution(board, skills):
    for skill in skills:
        mode, r1, c1, r2, c2, degree = skill
        for col in range(c1, c2 + 1):
            for row in range(r1, r2 + 1):
                if mode == 1:
                    board[col][row] -= degree
                else:
                    board[col][row] += degree
    answer = 0
    for bo in board:
        for idx in range(len(bo)):
            if bo[idx] > 0:
                answer += 1

    return answer


print(
    solution(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    )
)
