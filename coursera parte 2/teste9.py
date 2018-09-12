#!/usr/bin/env python3
# coding=utf-8


def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
        print(lista)
    return lista

numeros = [55,33,0,900,-432,10,77,2,11]

def fatorial(n):
    if n <= 1:
        return n
    else:
        return n * fatorial(n-1)

#print(selecao_direta(numeros))

#print(fatorial(10))

def x(n):
    if n == 0:
        print(n)
        return 0
    else:
        x(n-1)
        print(n)

#print(x(10))


def x(n):
    if n >= 0 or n <= 2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

#print(x(6))

def elefantes(n):
    if n <= 0: return ""
    if n == 1: return "Um elefante incomoda muita gente"+"\n"
    return elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) + ("muita gente" if n % 2 > 0 else "muito mais") + "\r\n"

def incomodam(n):
    if n <= 0: return ""
    if n == 1: return "incomodam "
    return "incomodam " + incomodam(n - 1)

print(elefantes(4))
