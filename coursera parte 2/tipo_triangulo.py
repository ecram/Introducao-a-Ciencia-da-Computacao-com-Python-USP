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


'''
if __name__ == '__main__':
    triangulo1 = Triangulo(1,2,3)
    triangulo2 = Triangulo(200,20,20)
    triangulo3 = Triangulo(10,10,10)

    print(triangulo1.perimetro())
    print(triangulo2.perimetro())
    print(triangulo3.perimetro())
    print(triangulo1.tipo_lado())
    print(triangulo2.tipo_lado())
    print(triangulo3.tipo_lado())
'''
