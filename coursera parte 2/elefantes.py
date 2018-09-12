#!/usr/bin/env python3
# coding=utf-8

aux = None

def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)


def elefantes(n):
    global aux
    if aux == None:
        aux = n
    if n < 1:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente" + "\n"
    else:
        return elefantes(n-1) + str(n) + " elefantes "+incomodam(n)+"muito mais" + "\n" + \
               (str(n) + " elefantes " + incomodam(1) + "muita gente" + "\n" if n != aux else "")


#print(elefantes(2),"\n")

'''
print("1. ",elefantes(4),"\n")
print("2. ",elefantes(-1),"\n")
print("3. ",elefantes(2),"\n")
print("4. ",elefantes(0),"\n")

Um elefante incomoda muita gente
2 elefantes incomodam incomodam muito mais
2 elefantes incomodam muita gente
3 elefantes incomodam incomodam incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam incomodam incomodam incomodam muito mais

'''
