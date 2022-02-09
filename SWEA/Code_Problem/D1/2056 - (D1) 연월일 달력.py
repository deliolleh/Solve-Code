# 테스트 케이스 수
N = int(input())

# 테스트 케이스
for i in range(1, N+1):
    ymd = input()
    year = ymd[0:4]
    month = ymd[4:6]
    day = ymd[6:8]
    if int(month) > 12 or int(month) < 1:
        print(f'#{i} -1')
        continue
    elif int(day) > 31 or int(day) < 1:
        print(f'#{i} -1')
        continue
    if int(month) == 2 and int(day) > 28:
        print(f'#{i} -1')
        continue
    else:
        print(f'#{i} {year}/{month}/{day}')
        continue