import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

sentencias = separa_sentencas(texto)
print("Separa sentencias: ", sentencias[1])

frases = separa_frases(sentencias[1])
print("Separa frases: ", frases[1])

palavras = separa_palavras(frases[1])
print("Separa palavras: ", palavras[0])
print("Todas palavras: ", palavras)

unicas = n_palavras_unicas(palavras)
print("N palavras únicas: ", unicas)

diferente = n_palavras_diferentes(palavras)
print("Tamanho da frequencia das n palavras diferentes", diferente)

# Inicia o programa
ass_cp = le_assinatura()
textos = le_textos()

palavras = separa_palavras(textos[0])
print(palavras)
soma = 0
for palavra in palavras:
    soma += len(palavra)
print(soma/len(palavras),end = "\n\n")

sentencias = separa_sentencas(textos[0])
frases = []
for sentencia in sentencias:
    frases.append(separa_frases(sentencia))
print(frases)
palavra2 = []
frases = [j for i in frases for j in i]
for frase in frases:
    palavra2.append(separa_palavras(frase))
palavra2 = [j for i in palavra2 for j in i]
print(palavra2)
soma = 0
for palavra in palavra2:
    soma += len(palavra)
print(soma/len(palavra2),end = "\n\n")
