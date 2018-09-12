#!/usr/bin/env python3
# coding=utf-8

def factorial(n):
    f = 1
    while n > 0:
        f = f * n
        n -= 1

    return f


if __name__ == '__main__':
    num = 1
    while num > 0:
        num = int(input("Digite um número: "))
        print("O factorial de ",num," é: ",factorial(num))

