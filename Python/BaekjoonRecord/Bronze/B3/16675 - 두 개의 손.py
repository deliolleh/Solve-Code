import sys

# 민성 두 손, 태경 두 손
m_l, m_r, t_l, t_r = map(str, sys.stdin.readline().split())

minsu = [m_l, m_r]
tae = [t_l, t_r]

if (
    ("S" in minsu and tae == ["P", "P"])
    or ("R" in minsu and tae == ["S", "S"])
    or ("P" in minsu and tae == ["R", "R"])
):
    print("MS")
elif (
    ("S" in tae and minsu == ["P", "P"])
    or ("R" in tae and minsu == ["S", "S"])
    or ("P" in tae and minsu == ["R", "R"])
):
    print("TK")
else:
    print("?")
