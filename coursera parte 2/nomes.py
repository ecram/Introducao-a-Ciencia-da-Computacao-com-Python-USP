#!/usr/bin/env python3
# coding=utf-8

def le_nomes(nomes):
    n = nomes[0].strip()
    min = len(n)

    for nome in nomes:
        if len(nome.strip()) < min:
            n = nome.strip()
            min = len(n)
    return n.capitalize()

lista = ["Marcelo Invert   ","    Daniel Augusto   "," San Jose                ","Caliman El Heroe","Chespitoss"]
print(le_nomes(lista))
