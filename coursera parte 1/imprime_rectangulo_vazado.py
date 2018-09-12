#!/usr/bin/env python3
# coding=utf-8
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux = 1
aux2 = 1

while aux <= altura :
    aux2 = 1
    while aux2 <= largura:
        if aux == 1 or aux == altura:
            print("#", end = "")
        elif aux2 == 1 or aux2 == largura:
            print("#", end = "")
        else:
            print(" ", end = "")
        aux2 += 1
    aux += 1
    print(end = "\n")
