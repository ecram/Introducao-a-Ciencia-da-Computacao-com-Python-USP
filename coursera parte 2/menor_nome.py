#!/usr/bin/env python3
# coding=utf-8

def menor_nome(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].replace(" ","")

    menor = lista[0]
    for p in lista:
        if len(p) < len(menor):
            menor = p

    return menor.capitalize()


'''
menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José
'''
