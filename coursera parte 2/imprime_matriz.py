#!/usr/bin/env python3
# coding=utf-8

def dimensoes(matriz):
    dimensao = []
    dimensao.append(len(matriz))
    dimensao.append(len(matriz[0]))
    return dimensao

def imprime_matriz(matriz):
    m = dimensoes(matriz)
    for i in range(m[0]):
        for j in range(m[1]):
            if (j+1) != len(matriz[0]):
                print(matriz[i][j], end = " ")
            else:
                print(matriz[i][j])
    pass

'''
minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)

1
2
3
'''
'''
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz2(minha_matriz)

1 2 3
4 5 6

'''
