# 입력받은 자연수 N
N = int(input())
# 생성자 존재시 알리는 flag
flag = 0

# N이하 숫자 중 생성자가 존재하는지 확인 N = num + (num의 각 자릿수의 합)이면 flag 발생
for num in range(1, N):
    create = num

    for i in str(num):
        create += int(i)
    if create == N:
        flag = 1
        break

if flag == 1:
    print(num)
else:
    print(0)
