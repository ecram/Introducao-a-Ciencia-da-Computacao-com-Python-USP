import random


def busca(lista, elemento):
    for i in range(len(lista) - 1):
        if lista[i] == elemento:
            return i
    return False


def lista_grande(n):
    return random.sample(range(n * 10), n)


def ordena(lista):
    for i in range(len(lista) - 1):
        min = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]

    return lista


def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def insertion_sort(lista):
    for i in range(1,len(lista)):
        j = i
        while j > 0  and lista[j-1] > lista[j]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
    return lista


'''
if __name__ == '__main__':
    print(insertion_sort(lista_grande(5)))
    print(insertion_sort(lista_grande(10)))
    print(insertion_sort(lista_grande(100)))

    print(bubble_sort(lista_grande(5)))
    print(bubble_sort(lista_grande(10)))
    print(bubble_sort(lista_grande(100)))

    print(ordena(lista_grande(5)))
    print(ordena(lista_grande(10)))
    print(ordena(lista_grande(100)))
    
    num = int(input("Digite a quantidade de números pseudo-aleatorios: "))
    print(lista_grande(num))
    
    lista = [1,2,3,4,5,6,7]
    print(busca(lista,3))
    lista = [1,2,3,5,4,6,7]
    print(busca(lista,8))
    lista = [5,4,3,2,1]
    print(busca(lista,-1))
'''
