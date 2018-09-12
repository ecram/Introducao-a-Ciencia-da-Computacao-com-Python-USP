#!/usr/bin/env python
# coding=utf-8
#import math

x1 = int(input("Digite o primeiro eixo X: "))
y1 = int(input("Digite o primeiro eixo y: "))
x2 = int(input("Digite o segundo eixo X: "))
y2 = int(input("Digite o segundo eixo y: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)

if distancia >= 10:
    print("longe")
else:
    print("perto")
