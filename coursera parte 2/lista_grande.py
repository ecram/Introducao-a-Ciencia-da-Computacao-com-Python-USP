import random

def busca(lista,elemento):
    for i in range(len(lista)-1):
        if lista[i] == elemento:
            return i
    return False

def lista_grande(n):
    return random.sample(range(n*10), n)


'''
if __name__ == '__main__':
    num = int(input("Digite a quantidade de números pseudo-aleatorios: "))
    print(lista_grande(num))
    
    lista = [1,2,3,4,5,6,7]
    print(busca(lista,3))
    lista = [1,2,3,5,4,6,7]
    print(busca(lista,8))
    lista = [5,4,3,2,1]
    print(busca(lista,-1))
'''
