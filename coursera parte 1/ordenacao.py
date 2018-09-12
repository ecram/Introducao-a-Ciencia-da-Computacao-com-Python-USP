# coding=utf-8
pri = int(input("Digite o primeiro numero: "))
seg = int(input("Digite o segundo numero: "))
ter = int(input("Digite o terceiro numero: "))

if pri <= seg and seg <= ter:
    print("crescente")
else:
    print("não está em ordem crescente")
