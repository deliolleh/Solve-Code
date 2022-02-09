# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 각 테스트 케이스마다 인원과 성적을 확인하고 싶은 번호 K를 입력받음
    N, K = map(int, input().split())

    # 중간 * 0.35 + 기말 * 0.45 + 과제 * 0.2의 합을 넣을 리스트 생성
    stu_ave = []
    for stu in range(N):
        a = list(map(int, input().split()))
        stu_ave.append(a[0] * 0.35 + a[1] * 0.45 + a[2] * 0.2)

    # 리스트는 0번부터 시작하므로, K번째 학생의 정보는 K-1번 index에 있다
    who = stu_ave[K-1]

    # 성적순으로 정리
    stu_ave.sort()

    # 정렬된 리스트에서 찾고 싶은 학생의 위치 조회
    score_tem = stu_ave.index(who)

    # N명의 학생이 있을 때 각 성적의 인원은 N/10이므로 성적별 위치는 위치 / 각 성적의 인원이다
    score = score_tem * 10 / N

    # score별 성적 입력
    if 0 <= score < 1:
        result = 'D0'
    elif 1 <= score < 2:
        result = 'C-'
    elif 2 <= score < 3:
        result = 'C0'
    elif 3 <= score < 4:
        result = 'C+'
    elif 4 <= score < 5:
        result = 'B-'
    elif 5 <= score < 6:
        result = 'B0'
    elif 6 <= score < 7:
        result = 'B+'
    elif 7 <= score < 8:
        result = 'A-'
    elif 8 <= score < 9:
        result = 'A0'
    else:
        result = 'A+'

    # 값 출력
    print(f'#{tc} {result}')
