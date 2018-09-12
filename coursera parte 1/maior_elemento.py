#!/usr/bin/env python3
# coding=utf-8

def maior_elemento(lista):
    maior = max(lista)
    return maior

if __name__ == '__main__':
    print("Introduzca la lista: ", end = "")
    lista = [int(x) for x in input().split()]
    print(maior_elemento(lista))
