class score:

    def __init__(self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math

    def total(self):
        return self.__korean + self.__english + self.__math

give = input().split(',')

Score = score(int(give[0]), int(give[1]), int(give[2]))

print("국어, 영어, 수학의 총점: {0}".format(Score.total()))