# 단어의 수
N = int(input())

# 알파벳들을 모아놓을 딕셔너리
letter_dict = dict()

# 각 단어를 받고
# 각 알파벳을 분석하면서 새로운 문자를 받았으면 딕셔너리를 생성하고
# 딕셔너리 키 값에 현재 자릿수에 대한 정보를 입력한다
for n in range(N):
    a = input()
    length = len(a)
    for i in range(length):
        if not letter_dict.get(a[i]):
            letter_dict[a[i]] = 0
        letter_dict[a[i]] += 10 ** (length - i - 1)

# 딕셔너리들의 value값들만 뽑아 리스트를 만든다
letter_list = []
for i in letter_dict.values():
    letter_list.append(i)
# 그리고 내림차순으로 정렬
letter_list.sort(reverse=True)

# idx = 0/ num = 9부터 시작해
# 큰 수부터 9를 곱해서 가장 큰 숫자를 만들어냄
i = 0
num = 9
res = 0
while i < len(letter_list) and num >= 0:
    res += letter_list[i] * num
    i += 1
    num -= 1

print(res)
