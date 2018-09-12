#!/usr/bin/env python3
# coding=utf-8

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibo(0) = ",fibonacci(0))
print("Fibo(1) = ",fibonacci(1))
print("Fibo(2) = ",fibonacci(2))
print("Fibo(3) = ",fibonacci(3))
print("Fibo(4) = ",fibonacci(4))
print("Fibo(5) = ",fibonacci(5))
print("Fibo(6) = ",fibonacci(6))
print("Fibo(7) = ",fibonacci(7))
print("Fibo(-1) = ",fibonacci(-1))

'''
print("Fibo(0) = ",fibonacci(4))
# deve devolver => 3
print(fibonacci(2))
# deve devolver => 1
'''
