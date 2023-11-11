while True:
    line_list = list(map(int, input().split()))

    if line_list == [0, 0, 0]:
        break

    line_list.sort()

    if line_list[0] ** 2 + line_list[1] ** 2 == line_list[2] ** 2:
        print("right")
    else:
        print("wrong")
