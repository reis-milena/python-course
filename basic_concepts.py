# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# nome = input("Diga-me seu nome: ")
# nome

a = 7
b = 2

a + b
a/b
a-b 
a%b
a//b
pow(a,b)

import math

math.log(10)

print("{:.2f}".format(math.log(10)))

import random

random.randint(1, 5)

random.randint?

for nota in range(1, 10):
    if nota <5:
        print("Vish, vc reprovou")
    elif nota >=5 and nota<6:
        print("Vc está de recuperação. Tente outra vez.")
    else:
        print("Parabéns, vc foi aprovado.")

valores = 1
while valores <10:
    print(valores)
    if valores <5:
        print("Quase lá.")
        valores = valores +1
    else:
        print("Vc chegou lá.")
        valores = valores +1
        
cargos = {"Analista": "João","Gerente": "Maria", "CEO": "Joana"}
print(cargos)
del cargos["CEO"]
print(cargos)


def compara(a,b):
    if a>b:
        print(a," é maior que ",b)
    elif a<b:
        print(a," é menor que ",b)
    else:
        print(a," é igual a ",b)
        
compara(1,3)
compara(5,4)
compara(100,100)

def area_quadrado(lado):
    area = lado**2
    print(area)
    
area_quadrado(3)

nova_area_quadrado = lambda lado: lado**2

nova_area_quadrado(3)

lados = [1,2,3,5,10]
perimetro_quadrado = list(map(lambda lado: lado*4, lados))
print(perimetro_quadrado)

multiplos_4 = [numero if numero %4 == 0 else "não é múltiplo" for numero in range(1,20)]
print(multiplos_4)

primeira_matriz = [[1,2],
             [3,4],
             [5,6]]
print(primeira_matriz)


import numpy as np

segunda_matriz = np.array([[1, 2, 3], [3, 4, 5]])
print(segunda_matriz)