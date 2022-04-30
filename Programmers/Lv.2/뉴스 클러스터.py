def solution(str1, str2):
    str1, str2 = list(str1.lower()), list(str2.lower())

    set1 = []
    set2 = []
    for idx1 in range(len(str1) - 1):
        element1 = ''.join(str1[idx1:idx1 + 2])
        if element1.isalpha():
            set1.append(element1)

    for idx2 in range(len(str2) - 1):
        element2 = ''.join(str2[idx2:idx2 + 2])
        if element2.isalpha():
            set2.append(element2)

    N = 0
    U = 0
    used = []

    for s1 in set1:
        if s1 not in used:
            if s1 in set2:
                N += min(set1.count(s1), set2.count(s1))
                U += max(set1.count(s1), set2.count(s1))
            else:
                U += set1.count(s1)
            used.append(s1)
    for s2 in set2:
        if s2 not in used:
            U += set2.count(s2)
            used.append(s2)
    try:
        answer = int(N / U * 65536)
    except ZeroDivisionError:
        answer = 65536
    return answer

