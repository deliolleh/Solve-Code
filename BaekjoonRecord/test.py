# def my_reverse(letter):
#     letter_list = list(letter)
#
#     for idx in range(len(letter_list) // 2):
#         letter_list[idx], letter_list[-1 - idx] = letter_list[-1 - idx], letter_list[idx]
#
#     return ''.join(letter_list)
#
#
# def my_reverse2(letter):
#     letter_rev = letter[len(letter) // 2]
#     for idx in range((len(letter) // 2) - 1, -1, -1):
#         letter_rev = letter[-1 - idx] + letter_rev + letter[idx]
#
#     return letter_rev
#
#
# str1 = 'algorithm'
# str2 = my_reverse(str1)
# str3 = my_reverse2(str1)
# print(str2)
# print(str3)
