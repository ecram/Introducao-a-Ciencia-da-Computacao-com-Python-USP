#!/usr/bin/env python3
# coding=utf-8


class Triangulo:
    def __init__(self,a,b,c):
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
            if c**2 == a**2 + b**2:
                return True
            else:
                return False
        elif a >= c and a >= b:
            if a**2 == b**2 + c**2:
                return True
            else:
                return False
        elif b >= a and b >= c:
            if b**2 == a**2 + c**2:
                return True
            else:
                return False
        else:
            return False

'''
if __name__ == '__main__':
    triangulo1 = Triangulo(1,3,4)
    triangulo2 = Triangulo(3,4,5)
    triangulo3 = Triangulo(10,10,10)

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
