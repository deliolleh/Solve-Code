import re


def solution(word, pages):
    answer = 0
    total_score = 0
    word = word.lower()
    for idx in range(len(pages)):
        pages[idx] = pages[idx].lower()

    def scoring(string):
        this = string.find('content="https://') + 17
        thisend = string.find("</head>") - 4
        here = string[this:thisend]
        basic = string.count(
            "^[a-zA-Z]" + word + "^[a-zA-z]", string.find("<body>"), string.find("<a")
        )
        linked = []
        for idx in re.finditer('<a href="https://', string):
            end = string.find('"', idx.end())
            linked.append(string[idx.end() : end])

        return [here, basic, linked]

    sites = []
    for idx in range(len(pages)):
        sites.append(scoring(pages[idx]))

    for site_idx in range(len(sites)):
        site_link_score = 0
        # for link_site in sites[site_idx][2]:
        #     for site_idx2 in range(len(sites)):
        #         if link_site == sites[site_idx2][0]:
        #             site_link_score += (sites[site_idx2][1] / len(sites[site_idx2][2]))
        for site_idx2 in range(len(sites)):
            if sites[site_idx][0] in sites[site_idx2][2]:
                site_link_score += sites[site_idx2][1] / len(sites[site_idx2][2])
        site_total = sites[site_idx][1] + site_link_score
        if site_total > total_score:
            total_score, answer = site_total, site_idx

    return answer


print(
    solution(
        "Muzi",
        [
            '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://careers.kakao.com/interview/list"/>\n</head>  \n<body>\n<a href="https://programmers.co.kr/learn/courses/4673"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>',
            '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://www.kakaocorp.com"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href="https://hashcode.co.kr/tos"></a>\n\n\t^\n</body>\n</html>',
        ],
    )
)
