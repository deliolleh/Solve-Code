from math import ceil


def solution(fees, records):
    answer = []
    cars = dict()
    get_time = dict()

    entry_time, entry_fee, count_time, count_fee = fees
    for record in records:
        # 각 원소를 받고
        time, car_num, check = record.split()
        # 시분을 분으로 통일
        in_time = int(time[0:2]) * 60 + int(time[3:])
        # IN => 입차 시간
        if check == 'IN':
            cars[car_num] = in_time
        # OUT => 출차, 기록된 입차시간만큼을 뺌
        else:
            get_time[car_num] = get_time.get(car_num, 0) + in_time - cars[car_num]
            # 같은 차가 올 수 있기 때문에, key 삭제
            cars.pop(car_num)

    # 23시 59분까지 나가지 않은 차들
    close_time = 60 * 23 + 59
    for car in cars.keys():
        get_time[car] = get_time.get(car, 0) + close_time - cars[car]

    for car1, time in get_time.items():
        # 기본 시간 이내
        if time <= entry_time:
            answer.append([car1, entry_fee])
        # 기본 시간 초과
        else:
            total_fee = entry_fee + ceil(((time - entry_time) / count_time)) * count_fee
            answer.append([car1, total_fee])

    # 차량번호가 작은 순서대로 금액만 출력
    answer = list(map(lambda x: x[1], sorted(answer, key=lambda x: int(x[0]))))

    return answer


print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
