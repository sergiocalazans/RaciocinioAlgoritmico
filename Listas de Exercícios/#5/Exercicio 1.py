# Exercício 1

'''
1.	Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4x4), 
e então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo índice é o 
mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e assim por diante. 
Mostre então a matriz, o vetor e a média aritmética do vetor.
'''

import random as rd

def criar_matriz(linhas, colunas):
    return [[rd.randint(10, 99) for _ in range(colunas)] for _ in range(linhas)]

def encontrar_valores(matriz):

    vetor = []
    j = 0
    while j <= 3:
        lista = []
        for i in range(0, len(matriz)):
            
            lista.append(matriz[i][j])
        
        vetor.append(max(lista))
        j += 1
    
    tamanho = len(matriz)
    soma = sum(vetor)
    media = soma / tamanho

    print(f"\nVetor de {tamanho} posições: {vetor}")
    print(f"A média dos valores do vetor: {media}")

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(str(elemento).zfill(2), end=' ')
        print()
    print()

matriz = criar_matriz(4, 4)

print("\nMatriz Original:")
imprimir_matriz(matriz)
encontrar_valores(matriz)
