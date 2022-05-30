# def solution(numbers):
#     # numbers의 가장 큰 원소의 자릿수
#     cnt = len(str(max(numbers)))
#     # 각 숫자의 가장 큰 자리의 수 1차 비교
#     # 같은 경우 (43, 44 / 최대 자릿수 3 => 434343[0:3] = 434 444444[0:3] = 444)
#     # 반복도 같은 경우(예: 30, 303 / 최대 자릿수 3 => 303030[0:3] = 303/ 303303303[0:3] = 303), 더 큰수가 앞으로
#     numbers.sort(key=lambda x: (int(str(x)[0]), int((str(x) * cnt)[0:cnt]), len(str(x))), reverse=True)
#     # 연결한 후 int화(0000같은 경우 제거)후 다시 string
#     answer = str(int(''.join(list(map(str, numbers)))))
#
#     return answer


# -----------------------------------
# def solution(numbers):
#     cnt = len(str(max(numbers)))
#     numbers.sort(key=lambda x: str(x) * cnt, reverse=True)
#     answer = str(int(''.join(list(map(str, numbers)))))
#
#     return answer


# ----------------------------------
def solution(numbers):
    # numbers의 가장 큰 원소의 자릿수
    cnt = len(str(max(numbers)))
    # 각 숫자의 가장 큰 자리의 수 1차 비교
    # 같은 경우 (43, 44 / 최대 자릿수 3 => 434343[0:3] = 434 444444[0:3] = 444)
    # 반복도 같은 경우(예: 30, 303 / 최대 자릿수 3 => 303030[0:3] = 303/ 303303303[0:3] = 303), 더 큰수가 앞으로
    numbers.sort(key=lambda x: int((str(x) * (cnt + 1))[0:cnt + 1]), reverse=True)
    # 연결한 후 int화(0000같은 경우 제거)후 다시 string
    answer = str(int(''.join(list(map(str, numbers)))))

    return answer


print(solution([3, 33, 333, 300, 303]))
