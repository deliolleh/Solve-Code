while True:
    html = input().strip()

    if html == '#':
        break

    state = 0
    tag = []

    while '<' in html:
        tag_start = html.find('<')
        tag_end = html.find('>')
        if html[tag_start+1] == 'a':
            tag.append('a')
        else:
            tag.append(html[tag_start+1:tag_end])
        html = html[tag_end+1:]

    while 'br /' in tag:
        tag.remove('br /')

    if len(tag) % 2 == 0:
        for idx in range(len(tag)//2):
            close = '/' + tag[idx]
            if close != tag[-1-idx]:
                state = 1
                break
    else:
        state = 1

    if state == 1:
        print('illegal')
    else:
        print('legal')
