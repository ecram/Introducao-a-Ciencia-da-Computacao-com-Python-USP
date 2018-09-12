#!/usr/bin/env python3
# coding=utf-8

def primeiro_lex(lista):
    menor = lista[0]

    for p in lista:
        if p < menor:
            menor = p

    return menor

'''
lista = ["ana", "maria", "Jose", "Valdemar"]
print(primeiro_lex(lista))
'''
