#!/usr/bin/env python3
# coding=utf-8

def maiusculas(frase):
    nova_frase = frase.replace(" ", "")
    so_maior = ""

    for p in nova_frase:
        if ord(p) >= 65 and ord(p) <= 90:
            print(p, end='')
            so_maior += p
    return so_maior


'''
maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'

'''
