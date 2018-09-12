#!/usr/bin/env python
# coding=utf-8

def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return "FizzBuzz"
    elif (n % 3 == 0) and (n % 5 != 0):
        return "Fizz"
    elif (n % 3 != 0) and (n % 5) == 0:
        return "Buzz"
    elif ((n % 3) != 0) and ((n % 5) != 0):
        return n

n = int(input("Digite uma número: "))

print(fizzbuzz(n))
