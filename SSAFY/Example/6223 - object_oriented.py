class Circle:

    def __init__(self, r):
        self.__r = r

    def total(self):
        return 3.14 * (self.__r**2)

circle = Circle(2)
print("원의 면적: {0}" .format(circle.total()))