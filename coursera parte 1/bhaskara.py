# coding=utf-8
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

raiz = b ** 2 - (4 * a * c)

if raiz == 0:
    raiz1 = (-b + (raiz) ** (0.5)) / (2 * a)
    print("a raiz desta equação é", raiz1)
elif raiz > 0:
    raiz1 = (-b + (raiz) ** (0.5)) / (2 * a)
    raiz2 = (-b - (raiz) ** (0.5)) / (2 * a)
    if raiz1 <= raiz2:
        print("as raízes da equação são", raiz1, "e", raiz2)
    else:
        print("as raízes da equação são", raiz2, "e", raiz1)
else:
    print("esta equação não possui raízes reais")
