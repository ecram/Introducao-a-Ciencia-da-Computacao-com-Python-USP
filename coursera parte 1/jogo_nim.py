#!/usr/bin/env python3
# coding=utf-8

# variables globales
n = 0
m = 0

def campeonato():
    count = 1
    ganhador = "nadie"
    pc = us = 0
    while count <= 3:
        print("\n" +"**** Rodada " + str(count) + " ****")
        ganhador = partida()
        if ganhador == "computador":
            pc += 1
        elif ganhador == "usuario":
            us += 1
        count += 1

    print("\n"+"Placar: Você "+str(us)+" X "+str(pc)+" Computador")


def computador_escolhe_jogada(n_local, m_local):
    global n
    n = n_local
    global m
    m = m_local
    aux = 0
    if n >= m + 1:
        aux = n % (m + 1)
    elif n <= m:
        aux = n

    if aux == 1:
        print("\n"+"O computador tirou uma peça.")
    else:
        print("\n"+"O computador tirou "+str(aux)+" peças.")

    n -= aux
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n > 1:
        print("Agora restam "+str(n)+" peças no tabuleiro.")

    return aux


def usuario_escolhe_jogada(n_local, m_local):
    global n
    n = n_local
    global m
    m = m_local
    pecas = 0
    while pecas < 1 or pecas > m:
        pecas = int(input("\nQuantas peças você vai tirar? "))
        if pecas > m:
            print("\n"+"Oops! Jogada inválida! Tente de novo.")

    n -= pecas
    if pecas == 1:
        print("Você tirou uma peça.")
    else:
        print("Voce tirou "+str(pecas)+" peças.")

    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n > 1:
        print("Agora restam "+str(n)+" peças no tabuleiro.")

    return pecas


def partida():
    global n
    n = int(input("\nQuantas peças? "))
    global m
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("\n"+"Voce começa!")
        while n > 0:
            usuario_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "usuario"
            computador_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
    else:
        print("\n"+"Computador começa!")
        while n > 0:
            computador_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
            usuario_escolhe_jogada(n, m)
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "usuario"

# programa principal
if __name__ == '__main__':
    print("Bem-vindo ao jogo do NIM! Escolha:\n")

    print("1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato "))

    if opcao == 1:
        print("\n" + "Voce escolheu uma partida!\n")
        partida()
    elif opcao == 2:
        print("\n" + "Voce escolheu um campeonato!\n")
        campeonato()
