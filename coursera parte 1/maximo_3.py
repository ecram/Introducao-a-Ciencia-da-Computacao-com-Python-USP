#!/usr/bin/env python
# coding=utf-8

def maximo(num1,num2,num3):
    if num1 >= num2 and num3 <= num1:
        return num1
    elif num2 >= num1 and num3 <= num2:
        return num2
    elif num3 >= num1 and num2 <= num3:
        return num3


num1 = int(input("Digite um número inteiro num1: "))
num2 = int(input("Digite um número inteiro num2: "))
num3 = int(input("Digite um número inteiro num3: "))

print(maximo(num1,num2,num3))
