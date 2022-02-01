A = input()
B = input()
A_rsp = input()
B_rsp = input()

def result_rsp(a, b):
    rsp = ["가위","바위", "보"]
    if (a == rsp[0] and b == rsp[2]) or (a == rsp[2] and b == rsp[0]):
        return print("가위가 이겼습니다!")
    elif (a == rsp[1] and b == rsp[0]) or (a == rsp[0] and b == rsp[1]):
        return print("바위가 이겼습니다!")
    elif (a == rsp[2] and b == rsp[1]) or (a == rsp[1] and b == rsp[2]):
        return print("보가 이겼습니다!")
    else: return print("무승부입니다!")


result_rsp(A_rsp, B_rsp)