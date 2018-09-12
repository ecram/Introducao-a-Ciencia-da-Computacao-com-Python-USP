# coding=utf-8
def numero():
    # num = int(input("Digite un numero triangular entero positivo: "))
    for num in range(6,1001):
        aux = 1
        producto = 1
        while producto < num:
            producto = aux * (aux + 1) * (aux + 2)
            if producto == num:
                print("Sus numeros del numero triangular ", num, " es: ", aux, aux + 1, aux + 2)
                break;
            aux += 1


if __name__ == '__main__':
    numero()
