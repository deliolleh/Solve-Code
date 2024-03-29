def solution(s):
    answer = 1000
    for length in range(1, len(s) + 1):
        now = ""
        conti = 1
        j = 0
        for i in range(length, len(s), length):
            if s[i : i + length] == s[i - length : i]:
                conti += 1
            else:
                if conti == 1:
                    now += s[i - length : i]
                else:
                    now += (
                        str(conti) + s[i - length : i]
                        if conti > 1
                        else s[i - length : i]
                    )
                    conti = 1
            j += length
        else:
            now += str(conti) + s[j:] if conti > 1 else s[j:]

        answer = min(answer, len(now))

    return answer


print(solution("abcabcdede"))
