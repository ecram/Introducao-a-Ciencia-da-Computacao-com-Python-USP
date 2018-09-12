#!/usr/bin/env python3
# coding=utf-8

def dimensoes(matriz):
    dimensao = []
    dimensao.append(len(matriz))
    dimensao.append(len(matriz[0]))
    return dimensao

def soma_matrizes(m1,m2):
    da = dimensoes(m1)
    db = dimensoes(m2)
    matriz = []
    if da[0] == db[0] and da[1] == db[1]:
        for i in range(da[0]):
            linha = []
            for j in range(da[1]):
                aux = m1[i][j] + m2[i][j]
                linha.append(aux)
            matriz.append(linha)
        return matriz
    else:
        return False


print("Teste 1:")
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))

print("Teste 2:")
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))

#soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]
'''
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => False
'''
