# 주어진 문자열의 수
N = int(input())

# 마디의 길이
length = 0

for i in range(1, N+1):
    letter = input()
    # le번째 단어가 letter[0]과 같고
    # letter[0: le]가 letter[le: le + le]와 같으면 0 ~ le-1의 길이 (le-1) - 0 + 1 을 length에 저장하고 출력
    # 결과가 나왔으면 시간 단축을 위해 break 사용
    for le in range(1, len(letter)-1):
        if letter[le] == letter[0] and letter[0:le] == letter[le:2*le]:
            length = le
            print(f'#{i} {le}')
            break
