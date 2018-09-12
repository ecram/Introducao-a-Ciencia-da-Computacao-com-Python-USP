#!/usr/bin/env python3
# coding=utf-8

lista = [5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
lista2 = [0, 1, 2, 3, 4]
lista1 = [0, -1, 2, -3, -4]
max = lista[0]
lim_inferior = 0
lim_superior = 0

for i in range(0,len(lista)):
    for j in range(i,len(lista)):
        if sum(lista[i:j]) > max:
            lim_inferior = i
            lim_superior = j
            max = sum(lista[i:j])

print("Limite inferior: ",lim_inferior)
print("Limite superior: ",lim_superior)

print("A suma da ",lista[lim_inferior:lim_superior]," é: ", sum(lista[lim_inferior:lim_superior]))
