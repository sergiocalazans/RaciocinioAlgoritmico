# Exercício 5

'''
4.	Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5x5) 
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro versões do programa): mostre a matriz original, 
mostre a matriz apenas com os valores que estão na parte hachurada e mostre a soma destes valores:
'''

import random as rd

qtdLinhas = 5
qtdColunas = 5

def criar_matriz(linhas, colunas):
    return [[rd.randint(10, 99) for _ in range(colunas)] for _ in range(linhas)]

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(str(elemento).zfill(2), end=' ')
        print()
    print()

def filtrar_matriz(matriz, tipo):
    filtrada = []
    soma = 0
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            if tipo == 'a' and (i == 2 or j == 2):  # cruz
                linha.append(valor)
                soma += valor
            elif tipo == 'b' and (i == 0 or i == 4 or j == 0 or j == 4):  # moldura
                linha.append(valor)
                soma += valor
            elif tipo == 'c' and (i == j or i + j == 4):  # diagonais
                linha.append(valor)
                soma += valor
            elif tipo == 'd' and (i + j) % 2 == 0:  # tabuleiro de xadrez
                linha.append(valor)
                soma += valor
            else:
                linha.append(0)
        filtrada.append(linha)
    return filtrada, soma

def matriz(tipo):
    
    global matriz_original

    filtrada, soma = filtrar_matriz(matriz_original, tipo)
    print(f"Matriz {tipo.upper()}:")
    imprimir_matriz(filtrada)

    print(f"Soma dos elementos hachurados: {soma}\n{'-'*40}")

matriz_original = criar_matriz(qtdLinhas, qtdColunas)

matriz('a')
matriz('b')
matriz('c')
matriz('d')
