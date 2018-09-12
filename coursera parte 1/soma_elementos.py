#!/usr/bin/env python3
# coding=utf-8

def soma_elementos(lista):
    soma = sum(lista)
    return soma

if __name__ == '__main__':
    print("Introduzca la lista: ", end = "")
    lista = [int(x) for x in input().split()]
    print(soma_elementos(lista))
