#!/usr/bin/env python
# coding=utf-8

def maximo(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Digite um número inteiro num1: "))
num2 = int(input("Digite um número inteiro num2: "))

print(maximo(num1,num2))
