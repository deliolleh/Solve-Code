# def my_sum(n):
#     if n ==1:
#         return 1
#     return n + my_sum(n-1)
#
# print(my_sum(23))

# pratice3 - 회문 판별
# def is_pal_recursive(word):
#     word_list = list(word)
#     if word == []:
#         return True
#     if word[0] != word[-1]:
#         return False
#     else:
#         word_list.pop(0)
#         word_list.pop(-1)
#         return is_pal_recursive(word)
#
# print(is_pal_recursive('tomato'))
# print(is_pal_recursive('racecar'))
# print(is_pal_recursive('azza'))

# Workshop4 1
# def get_secret_word(arr):
#     total = ''
#     for num in arr:
#         total += chr(num)
#     return total
#
# print(get_secret_word([83, 115, 65, 102, 89]))

# Wordkshop 2
# def get_secret_number(word):
#     total = 0
#     word_list = list(word)
#     for one in word_list:
#         total += ord(one)
#     return total
#
# print(get_secret_number('tom'))

# Workshop 3
# def get_strong_word(a, b):
#     ascii_a = 0
#     for i in a:
#         ascii_a += ord(i)
#     ascii_b = 0
#     for i in b:
#         ascii_b += ord(i)
#     if ascii_a > ascii_b:
#         return a
#     else:
#         return b
#
# print(get_strong_word('z', 'a'))
# print(get_strong_word('tom', 'john'))

# Practice1 1-2
# def my_all(elements):
#     if len(elements) == 0:
#         return True
#     for element in elements:
#         if bool(element) == True:
#             return True
#         else:
#             return False
#
# print(my_all([]))
# print(my_all([1, 2, 5, '6']))
# print(my_all([[], 2, 5, '6']))
# print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

# Practice1 1-3
# def my_any(elements):
#     for element in elements:
#         if element == 0 or element == '':
#             return False
#         else:
#             return True
#
#
# print(my_any([1, 2, 5, '6']))
# print(my_any([[], 2, 5, '6']))
# print(my_any([0]))
# print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))

print(1 % 10)