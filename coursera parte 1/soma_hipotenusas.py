#!/usr/bin/env python3
# coding=utf-8

def e_hipotenusa(num):
    aux1 = 1

    while aux1 <= num:
        aux2 = 1
        while aux2 <= num:
            hipo = (aux1 ** 2 + aux2 ** 2) ** (0.5)
            if hipo == num:
                return True
            aux2 += 1
        aux1 += 1

    return False

def soma_hipotenusas(num):
    aux = 1
    soma = 0

    while aux <= num:
        if e_hipotenusa(aux):
            soma += aux
        aux += 1
    return soma

if __name__ == '__main__':
    num = int(input("Digite um numero: "))

    print(soma_hipotenusas(num))
