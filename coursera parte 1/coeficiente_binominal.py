#!/usr/bin/env python
# coding=utf-8

def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


def binominal(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


if __name__ == '__main__':
    n = int(input("Digite um número inteiro n: "))
    k = int(input("Digite um número inteiro k: "))

    print(binominal(n, k))
