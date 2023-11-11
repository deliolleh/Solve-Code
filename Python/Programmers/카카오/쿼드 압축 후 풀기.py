def solution(arr):
    answer = [0, 0]

    def grid(y, x, size):
        nonlocal answer
        for i in range(size):
            for j in range(size):
                if arr[y + i][x + j] != arr[y][x]:
                    grid(y, x, size // 2)
                    grid(y + size // 2, x, size // 2)
                    grid(y, x + size // 2, size // 2)
                    grid(y + size // 2, x + size // 2, size // 2)
        answer[arr[y][x]] += 1

    grid(0, 0, len(arr))

    return answer


solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])


def solution(arr):
    global answer
    answer = [0, 0]
    quad(arr, answer, len(arr))
    return answer


def quad(arr, s, n):
    x, y, tg = s[0], s[1], arr[s[0]][s[1]]
    for i in range(n):
        for j in range(n):
            if arr[x + i][y + j] != tg:
                quad(arr, [x, y], n // 2)
                quad(arr, [x, y + n // 2], n // 2)
                quad(arr, [x + n // 2, y], n // 2)
                quad(arr, [x + n // 2, y + n // 2], n // 2)
                return
    answer[tg] += 1
