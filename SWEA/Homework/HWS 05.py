## Homework

# 1. 모음은 몇 개나 있을까

# def count_vowels(letter):
#     cnt = 0
#     list_letter = list(letter)
#     cnt += list_letter.count('a')
#     cnt += list_letter.count('e')
#     cnt += list_letter.count('i')
#     cnt += list_letter.count('o')
#     cnt += list_letter.count('u')
#     return cnt
#
#
# print(count_vowels('apple'))
# print(count_vowels('banana'))

# 3. 정사각형만 만들기
#
# def only_square_area(x, y):
#     ans = []
#     for one in x:
#         for another in y:
#             if one == another:
#                 ans.append(one ** 2)
#             else:
#                 pass
#
#     return ans
#
# print(only_square_area([32, 55, 63], [13, 32, 40, 55]))

# Workshop

# 1. 평균 점수 구하기
#
# def get_dict_avg(dict):
#     length = 0
#     total = 0
#     for key, value in dict.items():
#         length += 1
#         total += value
#
#     return print(total/length)
#
#
# get_dict_avg({'python': 80, 'algorithm': 90, 'django': 89, 'web': 83})

# 2. 혈액형 분류하기
# def count_blood(List):
#     blood_a = List.count('A')
#     blood_b = List.count('B')
#     blood_o = List.count('O')
#     blood_ab = List.count('AB')
#
#     dict_blood = {'A': blood_a, 'B': blood_b,
#                   'O': blood_o, 'AB': blood_ab}
#     return dict_blood
#
#
# print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB',
#              'O', 'A', 'B', 'O', 'B', 'AB']))
