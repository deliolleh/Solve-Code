import sys

N, L = map(int, input().split())

area = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
stated = [[0] * N for _ in range(N)]

result = 0


def check(arr):
    # 위 아래는 index 위치만 다르고 동일하므로 위에만 설명
    index = 1

    # 경사로 사용여부 확인
    used = [0 for _ in range(N)]

    while index < N:
        # 높이가 같으면 다음 바로 진행
        if arr[index - 1] == arr[index]:
            index += 1

        # 좌측이 높다
        # 우측 L칸이 존재하고
        # 경사로가 놓여있지 않은지 체크 => 근데 얘는 필요 없을듯 => 삭제해도 문제가 없었다
        elif arr[index - 1] - arr[index] == 1:
            for runaway_r in range(L):
                # 범위를 초과하거나, L칸 내에 높이가 다른 칸이 있으면 0 반환
                if index + runaway_r >= N or arr[index] != arr[index + runaway_r]:
                    return 0
                # 일치한다면 경사로가 놓일 것이므로 used 체크
                # 처음엔 중간에 빠져나가면 어떻게 해야할까 싶었는데 어짜피 used도 초기화된다
                # 상관 없네
                used[index + runaway_r] = 1
            # L칸을 다 조사했으므로 그 다음 칸에 대해 체크
            index += L

        # 우측이 높다
        # 좌측 L칸에 대해 체크
        # 좌측은 지나왔던 칸이므로 경사로가 존재할 수 있다
        elif arr[index - 1] - arr[index] == -1:
            for runaway_l in range(L):
                # 범위를 초과하거나, L칸 내에 높이가 다른 칸이 있거나 이미 경사로가 놓였다면 0 반환
                if index - 1 - runaway_l < 0 or arr[index - 1] != arr[index - 1 - runaway_l] or used[
                    index - 1 - runaway_l]:
                    return 0
                used[index - 1 - runaway_l] = 1
            # 이 경우는 새로운 칸에 대한 탐색이 없었으므로 바로 다음 칸으로 이동
            index += 1
        else:
            return 0

    # while 문을 빠져나오면 1 반환
    return 1


for i in range(N):
    # i행, i열을 분석하면서 길이면 1, 아니면 0을 반환(i마다 최대 2 적립 가능)
    result += check(area[i]) + check([area[j][i] for j in range(N)])

print(result)
