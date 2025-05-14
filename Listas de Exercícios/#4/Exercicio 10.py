# Exercício 10

'''
10.	Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores positivos. 
Modifique então o vetor de forma que, tenhamos primeiro todos os números pares, depois, os números impares. 
Mostre o vetor antes e depois da modificação.
'''

from random import randint

# Entrada
print()
vLido = [-1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
vNovo = []
j = 0

for i in vLido:
    novo_item = randint(1, 10)

    if i < 0:
        vLido[j] = novo_item
        print(f"Novo valor {novo_item} está substituindo {i} no vetor.")
    
    j += 1

# Processamento

for valor in vLido:
    if valor % 2 == 0:
        vNovo.append(valor)
    
for valor in vLido:
    if valor % 2 != 0:
        vNovo.append(valor)

# Saída

print(f"\nO vetor antigo: \n{vLido}\n")
print(f"\nO vetor novo: \n{vNovo}\n")