#!/usr/bin/env python3
# coding=utf-8
import random

def lista_grande(n):
    return random.sample(range(n * 10), n)

def encontra_impares(lista):
    impares = []
    if len(lista) > 0:
        if lista[0] % 2 == 1:
            impares.append(lista[0])

        return impares + encontra_impares(lista[1:])
    return impares


'''
if __name__ == '__main__':
    print(encontra_impares([1,-1,2,-2,3,-3,4,-4]))

    print(soma_lista([1,-1,2,-2,3,-3,4,-4]))
    print(soma_lista(lista_grande(10)))
    print(soma_lista(lista_grande(4)))
'''
