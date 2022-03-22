# 완전 이진 트리에서의 순회
"""
6 5
1 2 1 3 2 4 2 5 3 6
"""


def pre_order(v):
    global last
    if v <= last:
        print(v)
        pre_order(v * 2)
        pre_order(v * 2 + 1)
