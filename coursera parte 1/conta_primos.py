#!/usr/bin/env python3
# coding=utf-8

def primos(n):
    count = 2
    while count < n:
        if n % count == 0:
            return False
        else:
            count += 1
    return True

def n_primos(num):
    aux = 1
    count = 0

    while aux < num:
        aux += 1
        if primos(aux):
            count += 1

    return count


if __name__ == '__main__':
    num = int(input("Digite um número mayor a 2: "))


    print(n_primos(num))

