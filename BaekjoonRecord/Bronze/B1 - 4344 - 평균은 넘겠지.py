TC = int(input())

for tc in range(TC):
    students, *score = map(int, input().split())

    ave = sum(score) / students

    pass_stu = 0
    for sco in score:
        if sco > ave:
            pass_stu += 1

    pass_per = pass_stu/students * 100

    print(f'{pass_per:.3f}%')
