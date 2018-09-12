#!/usr/bin/env python3
# coding=utf-8
import random

def lista_grande(n):
    return random.sample(range(n * 10), n)

def busca_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


def busca(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        centro = (inicio + fim) // 2
        print(centro)
        if lista[centro] == elemento:
            return centro
        else:
            if elemento < lista[centro]:
                fim = centro - 1
            else:
                inicio = centro + 1

    return False


def busca_binaria(lista, elemento, inicio=0, fim=None):
    if fim == None:
        fim = len(lista) - 1

    if fim < inicio:
        return False
    else:
        centro = inicio + (fim - inicio) // 2

    if lista[centro] > elemento:
        return busca_binaria(lista, elemento, inicio, centro - 1)
    elif lista[centro] < elemento:
        return busca_binaria(lista, elemento, centro + 1, fim)
    else:
        return centro


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo,lado_direito[1:])


if __name__ == '__main__':
    print(merge_sort(lista_grande(5)))
    print(merge_sort(lista_grande(10)))

    '''
    print(busca_binaria(['a', 'e', 'i'], 'e'), "\n\n")
    # 1
    # deve devolver => 1

    print(busca_binaria([1, 2, 3, 4, 5], 6), "\n\n")
    # 2
    # 3
    # 4
    # deve devolver => False
    print(busca_binaria([1, 2, 3, 4, 5, 6], 4), "\n\n")
    # 2
    # 4
    # 3
    # deve devolver => 3
    
    lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(busca(lista, 100))
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(busca(lista, 3))
    lista = [1, 2, 3, 5, 4, 6, 7]
    print(busca(lista, 8))
    lista = [5, 4, 3, 2, 1]
    print(busca(lista, -1))
    '''
