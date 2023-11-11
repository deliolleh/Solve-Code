# 실제 패스워드, 입력 시작 번호
password, start = map(int, input().split())

# 초기값부터 시작하므로 1을 더한다
print(abs(password-start+1))
