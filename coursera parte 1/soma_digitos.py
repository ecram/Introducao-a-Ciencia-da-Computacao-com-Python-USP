#!/usr/bin/env python
# coding=utf-8

n = int(input("Digite o valor de n: "))

suma = 0

while n > 0:
    suma += (n % 10);
    n = int(n / 10)

print(suma)
