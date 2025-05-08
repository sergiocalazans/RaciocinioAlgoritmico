'''
---------------------------------------------------------------
Desafio: Desenvolver um algoritmo que lê um vetor de 10 números 
inteiros e retorna uma lista com os elementos pares
---------------------------------------------------------------
'''

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = []

for valor in v:

    if valor % 2 == 0:
        l.append(valor)

print(v)
print(len(v))

print(l)
print(len(l))