for tc in range(1, int(input()) + 1):
    N = int(input())

    # 이진 트리 배열
    nodes = [0] * (N + 1)

    # 이진 트리의 높이를 계산하는 변수
    height = 0
    for i in range(11):
        if 2 ** i <= N <= 2 ** (i+1) - 1:
            height = i

    # 들어갈 숫자 변수
    now = 1
    # 높이의 첫번째 노드에 위치
    lo = 2 ** height

    # 모든 수를 다 채울 때까지 => 중위 순회 방식
    while now <= N:
        # 왼쪽 자식 노드가 있을 때 우선 처리
        if 2 * lo <= N and nodes[2*lo] == 0:
            lo = lo * 2
            continue
        # nodes[lo]가 0일 때 now 할당
        if nodes[lo] == 0:
            nodes[lo] = now
            now += 1
        # 오른쪽 자식 노드가 있으면 다시 내려감
        if 2 * lo + 1 <= N and nodes[2*lo+1] == 0:
            lo = 2 * lo + 1
        # 없다면 상위 노드로 이동
        else:
            lo = lo // 2

    print(f'#{tc} {nodes[1]} {nodes[N//2]}')
