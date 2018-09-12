#!/usr/bin/env python
# coding=utf-8

n = int(input("Digite um número inteiro: "))

count = 2
primo = True

while count < n:
    if n % count == 0:
        primo = False
        break
    else:
        count += 1

if primo:
    print("primo")
else:
    print("não primo")
