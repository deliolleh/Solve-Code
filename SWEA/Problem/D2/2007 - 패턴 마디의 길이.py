# 주어진 문자열의 수
N = int(input())

# 마디의 길이
length = 0

for i in range(1, N+1):
    letter = input()
    for le in range(1, len(letter)-1):
        if letter[le] == letter[0] and letter[le+1] == letter[1]:
            length = le
            print(f'#{i} {le}')
            break
