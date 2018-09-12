#!/usr/bin/env python3
# coding=utf-8

primos = [2, 3, 5, 7, 11]
i = 0
while i < len(primos):
    print( "elemento de indice %d = %d"%(i, primos[i]) )
    i = i + 1

print("\n")
primos = [2, 3, 5, 7, 11, 13]
for elem in primos:
    print( elem )

print("\n")
primos = [2, 3, 5, 7, 11, 13]
for i in range(len(primos)):
    print( "primo [%d]: %d"%(i,primos[i]) )
