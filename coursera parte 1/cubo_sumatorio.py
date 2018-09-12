#!/usr/bin/env python3
# coding=utf-8

def cubo(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * 2 + cubo(num - 1)


if __name__ == '__main__':
    num = int(input("Digite um numero ao cubo: "))

    aux = cubo(num - 1)
    aux2 = 1

    print(num, "** 3: ", end="")
    if num == 1:
        print(aux)
    else:
        while aux2 <= num:
            aux += 2
            if aux2 != num:
                print(aux,"+ ", end = "")
            else:
                print(aux, end = "")
            aux2 += 1
