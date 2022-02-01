name = input()
age = int(input())

def calc_year_hund(a):
    hund = 2019 - a +100
    return hund

print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name, calc_year_hund(age)))