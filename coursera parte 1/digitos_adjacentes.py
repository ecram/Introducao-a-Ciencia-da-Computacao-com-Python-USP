#!/usr/bin/env python
# coding=utf-8

n = int(input("Digite um número inteiro: "))

adjacente = False

while n > 0:
    aux = n % 10
    aux2 = int(n/10) % 10
    if aux == aux2:
        adjacente = True
        n = int(n/10)
    else:
        n = int(n/10)

if adjacente:
    print("sim")
else:
    print("não")
