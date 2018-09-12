# coding=utf-8
"""
# Nombre: ejercicio05
# Descripción: decena
# Fecha: 06/04/2018
"""

num_str = input("Digite um número inteiro: ")

num_int = int(num_str)

dec = (num_int % 100) // 10

print("O dígito das dezenas é",dec)
