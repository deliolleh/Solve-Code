from itertools import combinations


def solution(orders, course):
    menus = dict()
    for cnt in course:
        if list(map(lambda x: len(x) >= cnt, orders)).count(True) > 1:
            for order in orders:
                ideas = combinations(order, cnt)
                for idea in ideas:
                    new = ''.join(sorted(idea))
                    if menus.get(new, 0):
                        menus[new] += 1
                    else:
                        menus[new] = 1

    course_cnt = [0] * (course[-1] + 1)
    course_menu = [[] for _ in range(course[-1] + 1)]
    for key, value in menus.items():
        if course_cnt[len(key)] < value and value > 1:
            course_cnt[len(key)] = value
            course_menu[len(key)].clear()
            course_menu[len(key)].append(key)
        elif course_cnt[len(key)] == value:
            course_menu[len(key)].append(key)

    answer = sorted(sum(course_menu, []))

    return answer