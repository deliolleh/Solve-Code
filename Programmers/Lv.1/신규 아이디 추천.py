def solution(new_id):
    if new_id.isupper():
        new_id = new_id.lower()

    new2_id = ''
    for id in new_id:
        if 48 <= ord(id) <= 57 or 97 <= ord(id) <= 122 or ord(id) in [45, 46, 95]:
            new2_id += id

    while '..' in new2_id:
        new2_id.replace('..', '.')

    list_id = list(id)
    if list_id[0] == '.':
        list_id = list_id[1:]
    if list_id[-1] == '.':
        list_id = list_id[:len(list_id)]

    new3_id = ''.join(list_id)

    if new3_id == '':
        new3_id += 'a'

    list2_id = list(new3_id)
    if len(list2_id) > 15:
        list2_id = list2_id[:15]
        if list2_id[-1] == '.':
            list2_id = list2_id[:len(list2_id)]

    if len(list2_id) <= 2:
        while len(list2_id) < 3:
            list2_id += list2_id[-1]

    answer = ''.join(list2_id)

    return answer

