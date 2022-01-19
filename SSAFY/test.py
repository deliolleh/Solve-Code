# def rectangle(x_axis, y_axis):
#     area = x_axis * y_axis
#     round_rect = 2 * (x_axis + y_axis)
#     return area, round_rect
#
# print(rectangle(30, 20))

# Workshop3-2
# def dict_list_sum(student):
#     age_total = 0
#     for stu in student:
#         age_total += stu['age']
#     return age_total
#
# print(dict_list_sum(
#     [
#         {'name': 'kim', 'age': 12},
#         {'name': 'lee', 'age': 4}
#     ]
# ))

# Workshop3-3
# list_ex = [[1], [2,3], [4,5,6], [7,8,9,10]]
#
# def all_list_sum(li):
#     total = 0
#     for li1 in li:
#         for li2 in li1:
#             total += li2
#     return total
#
# print(all_list_sum(list_ex))

# Homeworkd3-2
# def get_middle_char(str):
#     length = len(str)
#     cnt = 0
#     ans = ''
#     if length%2:
#         middle = length // 2 + 1
#         for one in str:
#             cnt += 1
#             if cnt == middle:
#                 ans += one
#     else:
#         middle1 = length // 2
#         middle2 = length // 2 + 1
#         for one in str:
#             cnt += 1
#             if cnt == middle1 or cnt == middle2:
#                 ans += one
#     return ans
# print(get_middle_char('ssafy'))
# print(get_middle_char('coding'))

# Homework3-4
# def my_func(a, b):
#     c = a + b
#     print(c)
#
# result = my_func(3, 7)
# print(result)

# Homework3-5
# def my_avg(*num):
#     length = len(num)
#     total = sum(num)
#     return total / length
#
# print(my_avg(77, 83, 95, 80, 70))A

# Workshop3-1
def list_sum(list_num):
    total = 0
    for num in list_num:
        total += num
    return total

print(list_sum([1,2,3,4,5]))