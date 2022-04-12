TC = int(input())

for tc in range(TC):
    # 학생 수, 성적들
    students, *score = map(int, input().split())

    # 평균를 float 형태로
    ave = sum(score) / students

    # 평균 넘은 학생들 수를 체크
    pass_stu = 0
    for sco in score:
        if sco > ave:
            pass_stu += 1

    # 백분율로 정리
    pass_per = pass_stu/students * 100

    print(f'{pass_per:.3f}%')
