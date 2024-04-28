while True:
    N = int(input())

    # 0을 받음녀 종료
    if N == 0:
        break

    # 학회 구성원을 dict형식으로 저장
    names = dict()
    wanted = ''
    for i in range(N):
        get = input()
        name, members = get.split(":")[0], get.split(":")[1].split(".")[0].split(",")
        if i == 0:
            wanted = name
        names[name] = members

    # 첫 학회의 리스트
    wanted_members = names.get(wanted)

    while True:
        # 리스트 내에 다른 학회가 있으면
        # 그 학회에 대한 리스트를 불러온 후
        # 학회를 삭제하고 그 학회의 리스트를 넣음
        for one in wanted_members:
            something = names.get(one)
            if something:
                wanted_members.remove(one)
                wanted_members.extend(something)
                wanted_members = list(set(wanted_members))
                break

        else:
            break

    print(len(wanted_members))