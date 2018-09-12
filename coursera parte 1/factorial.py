#!/usr/bin/env python
# coding=utf-8

n = int(input("Digite o valor de n: "))

f = 1

while n > 0:
    f = f * n
    n -= 1

print(f)
