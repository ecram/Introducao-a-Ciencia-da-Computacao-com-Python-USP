#!/usr/bin/env python3
# coding=utf-8


class Triangulo:
    def __init__(self,lado_a,lado_b,lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        return self.a + self.b + self.c


'''
if __name__ == '__main__':
    triangulo1 = Triangulo(1,2,3)
    triangulo2 = Triangulo(200,20,20)

    print(triangulo1.perimetro())
    print(triangulo2.perimetro())
'''
