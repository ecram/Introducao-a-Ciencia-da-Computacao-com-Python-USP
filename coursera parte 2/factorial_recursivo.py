#!/usr/bin/env python3
# coding=utf-8


def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

'''
print("factorial(0) = ",fatorial(0))
print("factorial(1) = ",fatorial(1))
print("factorial(2) = ",fatorial(2))
print("factorial(3) = ",fatorial(3))
print("factorial(4) = ",fatorial(4))
print("factorial(5) = ",fatorial(5))
print("factorial(-1) = ",fatorial(-1))
'''
