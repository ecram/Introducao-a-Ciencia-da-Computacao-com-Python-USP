#!/usr/bin/env python3
# coding=utf-8

def conta_letras(frase, contar="vogais"):
    frase = frase.lower()
    vogais = ['a','e','i','o','u']
    count = 0

    for vogal in vogais:
        count += frase.count(vogal)

    if contar == "vogais":
        return count
    elif contar == "consoantes":
        return len(frase.replace(" ", ""))-count

'''
frase = 'programamos em python'
print(conta_letras(frase))
# deve devolver 6

print(conta_letras('programamos em python', 'vogais'))
# deve devolver 6

print(conta_letras('programamos em python', 'consoantes'))
# deve devolver 13

'''
