def solution(str1, str2):
    # 소문자 처리
    str1, str2 = list(str1.lower()), list(str2.lower())

    set1 = []
    set2 = []
    for idx1 in range(len(str1) - 1):
        # 2단어씩 뽑아내는데
        element1 = ''.join(str1[idx1:idx1 + 2])
        # 두 단어 모두 문자일 때 set에 추가
        if element1.isalpha():
            set1.append(element1)

    for idx2 in range(len(str2) - 1):
        element2 = ''.join(str2[idx2:idx2 + 2])
        if element2.isalpha():
            set2.append(element2)

    # N => 교집합 U => 합집합
    N = 0
    U = 0
    used = []

    for s1 in set1:
        if s1 not in used:
            # 공유되는 단어가 있다면
            if s1 in set2:
                # 양쪽의 단어 수를 세고
                # 큰 쪽은 합집합, 작은 쪽은 교집합에 더함
                N += min(set1.count(s1), set2.count(s1))
                U += max(set1.count(s1), set2.count(s1))
            else:
                # 없으면 교집합이 아니므로 합집합에 모두 추가
                U += set1.count(s1)
            used.append(s1)
    # 여기는 set1에 없는 단어만 계산
    # 모두 합집합행
    for s2 in set2:
        if s2 not in used:
            U += set2.count(s2)
            used.append(s2)

    try:
        answer = int(N / U * 65536)
    # U = 0 즉 들어온 셋이 둘 다 없으면
    # zeroDivisonError가 나타나기 때문에
    # 이를 따로 처리 -> 결론적으로 U = N = 공집합이므로
    # 자카드 유사도는 1
    except ZeroDivisionError:
        answer = 65536
    return answer

