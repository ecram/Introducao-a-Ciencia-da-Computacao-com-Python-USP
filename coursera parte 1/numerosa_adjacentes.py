# coding=utf-8
num = int(input("Digite un numero: "))
bool = 0

while num > 0:
    aux = num % 10;
    aux2 = (num/10)%10
    if aux == aux2:
        print(num, "tem digitos adjacentes")
        bool = 1
    num = num//10

if bool == 0:
    print(num, "nao tem digitos adjacentes")
