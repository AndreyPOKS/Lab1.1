import math as m


class MainClass():
    R = 0
    Y = 0
    """описание треугольника"""
    def __init__(self, a, c, b=0):
        """свойства треугольника"""
        self.a = a
        self.c = c
        self.b = m.sqrt(c * c - a * a)
        print(self.a)
        print(self.c)
        print(self.b)
    def Pir(self, pir = 0):
        """вычисление периметра"""
        self.pir = self.a + self.c +self.b
        print('Периметр =', self.pir)

    def Ugol(self):
        print(self.a, self.b, self.c)
        A = (self.a * self.a + self.c * self.c - self.b * self.b) / (2 * self.a * self.c)
        Y = (self.b * self.b + self.c * self.c - self.a * self.a) / (2 * self.c * self.b)
        A = m.degrees(A)
        Y = m.degrees(Y)
        B = 180 - (A + Y)
        print(A)
        print(B)
        print(Y)
        return A, Y, B
    def Krug(self):

        R = (self.a * self.a + self.b * self.b)/2
        R = m.sqrt(R)
        print(R)
        return R


