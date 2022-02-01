# Homework

# 1. Built-in 함수와 메서드
# numbers1 = [8, 2, 5, 4, 9, 6, 7]
# numbers2 = [8, 2, 5, 4, 9, 6, 7]
#
# print(sorted(numbers1))
# print(numbers1)
# print(numbers2.sort())
# print(numbers2)

# 2. .extend()와 .append()
# numbers1 = [1, 2, 3]
# numbers2 = [1, 2, 3]
# numbers3 = [1, 2, 3]
# numbers4 = [1, 2, 3]
#
# add_num = [4, 10]
# add_num1 = 'abs'
#
# numbers1.extend(add_num)
# print(numbers1)
# numbers2.extend(add_num1)
# print(numbers2)
# numbers3.append(add_num)
# print(numbers3)
# numbers4.append(add_num1)
# print(numbers4)

# 3. 복사가 잘 된건가?
# a = [1, 2, 3, 4,5 ]
# b = a
#
# a[2] = 5
#
# print(a)
# print(b)


# WorkShop

# 1. 무엇이 중복일까
# def duplicated_letters(letter):
#     # 간편하게 set을 통해 중복 단어를 제외하는 방법
#     dup_list = set( )
#     for one in letter:
#         # 1번 이상 반복된 단어를 철자에 추가
#         if letter.count(one) > 1:
#             dup_list.add(one)
#
#     return list(dup_list)
#
# ###############################
#
# def duplicated_letters(letter):
#     # 리스트만으로 중복단어를 뽑아내는 방법
#     dup_list = []
#     for one in letter:
#         # 1번 이상 반복되고, dup_list에 들어가지 않은 철자를 추가
#         if letter.count(one) > 1 and one not in dup_list:
#             dup_list.append(one)
#
#     return print(list(dup_list))
#
#
# duplicated_letters('apple')
# duplicated_letters('banana')

# 2. 소대소대

# def low_and_up(letter):
#     # idx를 대체할 변수
#     cnt = 0
#     # 글자를 쉽게 계산하기 위해 리스트 형태로 변환
#     change_letter = list(letter)
#     for one in letter:
#         if cnt % 2:
#             one_change = one.swapcase()
#             change_letter[cnt] = one_change
#         cnt += 1
#
#     return print(''.join(change_letter))
#
#
# low_and_up('apple')
# low_and_up('banana')

# 3. 솔로 천국 만들기
def lonely(people):
    # 솔로들을 맞이할 리스트 생성
    lonely_list = []
    # 커플들을 막을 플래그 생성
    flag = 0
    for i in range(len(people)-1):
        # i와 i+1의 값이 동일할 때 아직 확인이 안돼 플래그가 0일 때는
        # 리스트에 넣어주고 플래그를 세운 뒤에는 막는다
        if people[i] == people[i+1]:
            if flag == 0:
                lonely_list.append(people[i])
                flag = 1
            else:
                pass
        # i와 i+1이 다를 경우에도 i-1이 같았으면 flag가 존재하기 때문에
        # flag가 존재하지 않는 자만 들어올 수 있도록 조건 작성
        elif people[i] != people[i+1] and flag == 0:
            lonely_list.append(people[i])
        else:
            flag = 0
    return print(lonely_list)


lonely([1, 1, 3, 3, 0, 1, 1])
lonely([4, 4, 4, 3, 3])
lonely([1, 1, 1, 2, 2, 2, 2, 4, 7, 6])

# pratice 1 sum을 이용해 배열 풀기
# print(sum([[1, 4], [10, 5], [20, 30]], []))
# print(sum(sum([[1, 4], [10, 5], [20, 30]], [])))
