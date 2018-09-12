#!/usr/bin/env python3
# coding=utf-8
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux = largura

while altura > 0:
    while largura > 0:
        print("#", end = "")
        largura -= 1
    altura -= 1
    largura = aux
    print(end = "\n")
