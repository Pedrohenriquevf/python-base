#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
-----------------
Tabuada do 2
2
4
6
...
----------------
"""
__version__ = "0.1.1"
__author__ = "Pedro"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Possivel forma de criarmos, mais simles
numeros = list(range(1,11))
#print(numeros)

#for numero in numeros:
#    print("Tabuada do:", numero)
#    for outro_numero in numeros:
#        print(numero * outro_numero)
#    print("________")


#Forma mais adaptada de criarmos a tabuada
for n1 in numeros: 
    print("{:^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros: 
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)

