# -*- coding utf-8 -*-

# 15-15.py

class Studnet:

    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{0} (name: {1}, gender: {2}, height: {3}"\
            .format(self.__class__.name, self.name, self.gender, self.height)

students = [
    Studnet("홍길동", "남", 176.5),
    Studnet("이순신", "남", 188.5),
    Studnet("유관순", "여", 158.4),
    Studnet("강감찬", "남", 182.2),
]

for student in students:
    print(student)

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x : x.name):
    print(student)

print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x : x.name, reverse=True):
    print(student)

print("height로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x : x.height):
    print(student)

print("height로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x : x.height, reverse=True):
    print(student)