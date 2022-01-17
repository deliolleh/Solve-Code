class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return '이름: {0}' .format(self.name)

class Graduatestudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return super().__repr__() + ', 전공: {0}' .format(self.major)

Hong = Student('홍길동')
Yi = Graduatestudent('이순신', '컴퓨터')
print(Hong)
print(Yi)
