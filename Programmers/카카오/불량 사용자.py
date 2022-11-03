def solution(user_id, banned_id):
    answer = 0
    used = [0] * len(user_id)
    record = []

    def perm(cnt, arr):
        nonlocal used, answer, record
        # 밴된 인원들만큼 순열이 찾으면
        if cnt == len(banned_id):
            for idx in range(len(banned_id)):
                # 일단 아이디의 길이가 같아야함
                if len(arr[idx]) != len(banned_id[idx]):
                    return
                # 밴된 유저의 패턴이 *이 아닐 때, 유저의 idx의 값과 같아야한다
                for idx2 in range(len(banned_id[idx])):
                    if banned_id[idx][idx2] == "*":
                        continue
                    if arr[idx][idx2] != banned_id[idx][idx2]:
                        return

            # 한번도 return 되지 않았고
            # 이미 기록된 배열과 같은 것이 없으면
            # 이를 기록하고 answer 1 더한다
            else:
                if sorted(arr) not in record:
                    record.append(sorted(arr))
                    answer += 1

        # 순열 크기가 같아질 때까지 반복
        else:
            for next in range(len(user_id)):
                if not used[next]:
                    used[next] = 1
                    perm(cnt + 1, arr + [user_id[next]])
                    used[next] = 0

    # 순열
    for idx3 in range(len(user_id)):
        used[idx3] = 1
        perm(1, [user_id[idx3]])
        used[idx3] = 0

    return answer


print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    )
)
