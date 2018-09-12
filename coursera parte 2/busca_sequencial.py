#!/usr/bin/env python3
# coding=utf-8


def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


'''
if __name__ == '__main__':
    lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(busca(lista,100))
    lista = [1,2,3,4,5,6,7]
    print(busca(lista,3))
    lista = [1,2,3,5,4,6,7]
    print(busca(lista,8))
    lista = [5,4,3,2,1]
    print(busca(lista,-1))
'''
