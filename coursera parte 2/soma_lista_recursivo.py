#!/usr/bin/env python3
# coding=utf-8
import random

def lista_grande(n):
    return random.sample(range(n * 10), n)

def soma_lista(lista):
    if len(lista) == 1:
        num = lista[0]
        return num
    else:
        return lista[0] + soma_lista(lista[1:])


'''
if __name__ == '__main__':
    print(soma_lista([1,-1,2-2,3,-3,4,-4]))
    print(soma_lista(lista_grande(10)))
    print(soma_lista(lista_grande(4)))
'''
