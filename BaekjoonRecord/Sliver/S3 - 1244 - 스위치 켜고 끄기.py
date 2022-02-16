import sys

SWE = int(input())

swe_sta = [0] + list(map(int, sys.stdin.readline().split()))

N = int(input())

for peo in range(N):
    gen, num = map(int, input().split())

    if gen == 1:
        for idx in range(1, SWE + 1):
            if idx % num == 0:
                if swe_sta[idx] == 1:
                    swe_sta[idx] = 0
                else:
                    swe_sta[idx] = 1

    else:
        if num - 1 > SWE - num:
            check = SWE - num
        else:
            check = num - 1

        k = 0
        for i in range(1, check + 1):
            if swe_sta[num + i] != swe_sta[num - i]:
                break
            k += 1

        for j in range(k + 1):
            if j == 0:
                swe_sta[num] = swe_sta[num] - 1
                if swe_sta[num] < 0:
                    swe_sta[num] *= -1

            else:
                swe_sta[num + j] = swe_sta[num + j] - 1
                if swe_sta[num + j] < 0:
                    swe_sta[num + j] *= -1
                swe_sta[num - j] = swe_sta[num - j] - 1
                if swe_sta[num - j] < 0:
                    swe_sta[num - j] *= -1

swe_sta = swe_sta[1:]
while True:
    print(*swe_sta[:10])
    swe_sta = swe_sta[10:]
    if len(swe_sta) < 10:
        print(*swe_sta)
        break
