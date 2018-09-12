#!/usr/bin/env python3
# coding=utf-8


def ordenada(lista):
    ordenado = True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            ordenado = False
            return ordenado
    return ordenado


'''
if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7]
    print(ordenada(lista))
    lista = [1,2,3,5,4,6,7]
    print(ordenada(lista))
    lista = [5,4,3,2,1]
    print(ordenada(lista))
'''
