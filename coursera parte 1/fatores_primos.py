#!/usr/bin/env python3
# coding=utf-8

def primo(n):
    count = 2
    while count < n:
        if n % count == 0:
            return False
        else:
            count += 1
    return True



if __name__ == '__main__':
    num = int(input("Digite um número mayor a 2: "))
    aux = 1

    print("A descomposição de fatores primos de ", num, " é: ", end="")

    while num > 1:
        aux += 1
        if primo(aux):
            while num % aux == 0:
                num /= aux
                print(aux, end = " ")
