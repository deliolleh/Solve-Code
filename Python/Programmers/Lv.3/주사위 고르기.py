from itertools import combinations

# def solution(dice):
#     answer = []
#     length_t = len(dice)
#     length_h = len(dice) // 2
#     indexs = [i for i in range(length_t)]
#     combs = combinations(indexs, length_h)
#     count = 0
#     temp = 0
#
#     def select(dice, depth, A, B):
#         nonlocal length_t, temp
#         if depth == length_t:
#             if A > B:
#                 temp += 1
#
#         elif depth < length_t // 2:
#             for i in range(6):
#                 select(dice, depth + 1, A + dice[depth][i], B)
#
#         else:
#             for j in range(6):
#                 select(dice, depth + 1, A, B + dice[depth][j])
#
#
#     for comb in combs:
#         temp = 0
#         A = []
#         B = []
#         for index in indexs:
#             if index in comb:
#                 A.append(dice[index])
#             else:
#                 B.append(dice[index])
#         C = A + B
#
#         select(C, 0, 0, 0)
#         if temp > count:
#             answer = comb
#             count = temp
#
#     return list(map(lambda x: x + 1, answer))

def solution(dice):
    answer = []
    length_t = len(dice)
    length_h = len(dice) // 2
    indexs = [i for i in range(length_t)]
    combs = combinations(indexs, length_h)
    count = 0
    temp = 0

    def select(dice, depth, ssum):
        nonlocal add_a, add_b, A, B

        if depth == length_h:
            if dice == A:
                if ssum in add_a:
                    add_a[ssum] += 1

                else:
                    add_a[ssum] = 1

            else:
                if ssum in add_b:
                    add_b[ssum] += 1

                else:
                    add_b[ssum] = 1


        else:
            for i in range(6):
                select(dice, depth + 1, ssum + dice[depth][i])

    for comb in combs:
        temp = 0
        A = []
        B = []
        for index in indexs:
            if index in comb:
                A.append(dice[index])
            else:
                B.append(dice[index])

        add_a = dict()
        add_b = dict()
        select(A, 0, 0)
        select(B, 0, 0)

        for a in add_a.keys():
            for b in add_b.keys():
                if a > b:
                    temp += add_a[a] * add_b[b]

        if temp > count:
            answer = comb
            count = temp

    return list(map(lambda x: x + 1, answer))

print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))