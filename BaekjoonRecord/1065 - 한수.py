N = int(input())
i = 1
cnt = 0

while i <= N:
    if 1<= i <=99:
       cnt += 1
    else:
        a = i % 10
        b = (i // 10) % 10
        c = i // 100
        if (a-b) == (b-c):
            cnt +=1
    i += 1

print(cnt)