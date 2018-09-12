#!/usr/bin/env python3
# coding=utf-8

def remove_repetidos(lista):
    lista = list(set(lista))
    return sorted(lista)

if __name__ == '__main__':
    print("Introduzca la lista: ", end = "")
    lista = [int(x) for x in input().split()]
    print(remove_repetidos(lista))
