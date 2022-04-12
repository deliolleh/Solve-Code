# Test Case 수
T = int(input())

for t in range(T):
    # k, n을 한 줄씩 입력받음
    k = int(input())
    n = int(input())

    # 각 층의 모든 호수의 인원 리스트를 가진 리스트를 생성 => 여기서 n+1를 입력(1호부터 시작하기에 k호까지 포함해야함)
    # 이를 망각하고 밑 len(floor)+1을 해 오류를 발생시킴
    floor = [[] for i in range(k+1)]

    # 각 층에 대한 정보 입력
    for idx in range(len(floor)):
        room = 0
        for num in range(n):
            if idx == 0:
                floor[idx].append(num+1)
            else:
                room += floor[idx-1][num]
                floor[idx].append(room)

    print(floor[-1][-1])
