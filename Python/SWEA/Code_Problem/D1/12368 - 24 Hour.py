# T = int(input())
#
# for test_case in range(1, T+1):
#     A, B = map(int, input().split())
#     C = (A + B) % 24
#     print("#{0} {1}".format(test_case, C))

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    time = A + B
    if time >= 24:
        time -= 24
    elif time == 48:
        time == 0
    print("#{0} {1}". format(i, time))