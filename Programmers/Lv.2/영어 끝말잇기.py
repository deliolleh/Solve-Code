def solution(n, words):
    answer = [0, 0]
    people = [0] * n
    use_word = []

    now = 0
    for i in range(len(words)):
        # n = 7, now = 4 => now = 4 % 7 + 1 = 4 + 1 = 5
        now = now % n + 1
        # now 번 사람의 index는 now - 1
        people[now - 1] += 1
        # 조건s
        # 1. 첫 단어 이후 이전 단어 마지막 단어와 이번 단어 첫 단어가 같을 경우
        # 2. 이번에 말한 단어가 use_word에 이미 존재하거나
        # 3. 이번에 말한 단어 길이가 1인 경우
        # 조건에 걸렸으면 [(몇 번 째 사람), (그 사람이 말한 횟수)] 출력
        # 여기 i > 0 => i > 1로 해서 TestCase 1개 틀림
        if (
            (i > 0 and words[i - 1][-1] != words[i][0])
            or words[i] in use_word
            or len(words[i]) == 1
        ):
            answer = [now, people[now - 1]]
            break

        # 통과시 use_word에 글자 등록
        else:
            use_word.append(words[i])

    return answer


print(
    solution(
        5,
        [
            "hello",
            "observe",
            "effect",
            "take",
            "either",
            "recognize",
            "encourage",
            "ensure",
            "establish",
            "hang",
            "gather",
            "refer",
            "reference",
            "estimate",
            "executive",
        ],
    )
)
