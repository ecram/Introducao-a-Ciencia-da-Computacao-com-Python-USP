#!/usr/bin/env python3
# coding=utf-8

def soma_hipotenusa(num):
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


if __name__ == '__main__':
    num = int(input("Digite um numero: "))
    aux = 1
    soma = 0

    while aux <= num:
        if soma_hipotenusa(aux):
            soma += aux
        aux += 1
    print(soma)
