def counting_sort(a, b, k):
    counts = [0] * (k+1)

    # 카운팅
    for i in range(k+1):
        counts[i] = a.count(i)
    # 다른 방법
    # for i in range(len(a)):
    #    counts[a[i]] += 1

    # 누적 in counts
    for idx in range(1, len(counts)):
        counts[idx] += counts[idx-1]

    # 배치
    for j in range(len(b)-1, -1, -1):
        b[counts[a[j]]-1] = a[j]
        counts[a[j]] -= 1

    return b


# 입력 리스트
in_list = [0, 4, 1, 3, 1, 2, 4, 1]

# 정렬된 리스트
out_list = [0] * len(in_list)

print(counting_sort(in_list, out_list, max(in_list)))
