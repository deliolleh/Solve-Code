def solution(board):
    answer = 10 ** 9
    length = len(board)

    ey, ex = length, length
    direction = [0, 0]

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def build(y, x, price, where):
        nonlocal answer, direction
        if y == ey - 1 and x == ex - 1:
            answer = min(answer, price)

        elif price >= answer:
            pass

        else:
            new_price = price + 100
            for my, mx in d:
                ny, nx = y + my, x + mx
                if 0 <= ny < length and 0 <= nx < length and not board[ny][nx]:
                    board[ny][nx] = 2
                    if where == [0, 0] or abs(where[0]) == abs(my) and abs(where[1]) == abs(mx):
                        new_where = [my, mx]
                        build(ny, nx, new_price, new_where)

                    else:
                        new_where = [my, mx]
                        build(ny, nx, new_price + 500, new_where)
                    board[ny][nx] = 0

                else:
                    continue

    board[0][0] = 1
    build(0, 0, 0, direction)

    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
