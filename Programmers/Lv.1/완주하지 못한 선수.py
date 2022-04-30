def solution(participant, completion):
    # 참가자들을 기록한 딕셔너리
    player = dict()
    # participant에서 참가자 정보 등록
    for part in participant:
        if not player.get(part):
            player[part] = 1
        # 동명이인의 경우
        else:
            player[part] += 1

    # 도착한 사람들은 player에서 제거
    for comp in completion:
        player[comp] -= 1
        # player의 key값이 0이 되면 그 key 제거
        if player[comp] == 0:
            del player[comp]

    # 한 명만 남으므로 그 key를 answer에 등록
    answer = list(player.keys())[0]

    return answer


solution(["leo", "kiki", "eden"], ["eden", "kiki"])
