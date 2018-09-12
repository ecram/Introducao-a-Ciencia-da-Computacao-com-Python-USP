#!/usr/bin/env python3
# coding=utf-8


class Triangulo:
    def __init__(self, a, b, c):
        self.lado_a = a
        self.lado_b = b
        self.hipotenusa = c

    def perimetro(self):
        return self.lado_a + self.lado_b + self.hipotenusa

    def tipo_lado(self):
        if self.lado_a == self.lado_b and self.lado_a == self.hipotenusa:
            return "equilátero"
        elif self.lado_a == self.lado_b or self.lado_b == self.hipotenusa or self.lado_a == self.hipotenusa:
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        a = self.lado_a
        b = self.lado_b
        c = self.hipotenusa
        if c >= a and c >= b:
            if c ** 2 == a ** 2 + b ** 2:
                return True
            else:
                return False
        elif a >= c and a >= b:
            if a ** 2 == b ** 2 + c ** 2:
                return True
            else:
                return False
        elif b >= a and b >= c:
            if b ** 2 == a ** 2 + c ** 2:
                return True
            else:
                return False
        else:
            return False

    def semelhantes(self, tri2):
        t1 = []
        t2 = []

        t1.extend([self.lado_a, self.lado_b, self.hipotenusa])
        t2.extend([tri2.lado_a, tri2.lado_b, tri2.hipotenusa])

        t1.sort()
        t2.sort()
        print(t1," ", t2)

        if t1[0] <= t2[0]:
            if t2[0] / t1[0] == t2[1] / t1[1] and t2[0] / t1[0] == t2[2] / t1[2]:
                return True
            else:
                return False
        else:
            if t1[0] / t2[0] == t1[1] / t2[1] and t1[0] / t2[0] == t1[2] / t2[2]:
                return True
            else:
                return False
'''
if __name__ == '__main__':
    triangulo1 = Triangulo(1, 2, 3)
    triangulo2 = Triangulo(5, 15, 10)
    triangulo3 = Triangulo(30, 10, 20)

    print(triangulo1.semelhantes(triangulo2))
    print(triangulo2.semelhantes(triangulo3))
    print(triangulo1.semelhantes(triangulo3))


    print(triangulo1.perimetro())
    print(triangulo2.perimetro())
    print(triangulo3.perimetro())
    print(triangulo1.tipo_lado())
    print(triangulo2.tipo_lado())
    print(triangulo3.tipo_lado())
    print(triangulo1.retangulo())
    print(triangulo2.retangulo())
    print(triangulo3.retangulo())
    
'''
