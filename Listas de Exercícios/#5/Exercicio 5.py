# Exercício 5

'''
4.	Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5x5) 
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro versões do programa): mostre a matriz original, 
mostre a matriz apenas com os valores que estão na parte hachurada e mostre a soma destes valores:
'''

import random as rd

aMatriz = []
bMatriz = []
cMatriz = []
dMatriz = []

def criarMatrizes(matriz): 

    j = 1
    matriz_original = matriz(5, 5)

    for linha in matriz_original:
                
            lista = []
            valor = None

            if j == 3:
                valor = 0

            for elemento in linha:
                
                if valor == 0:
                    lista.append(str(elemento))
                elif elemento == linha[2]:
                    lista.append(str(elemento))
                else:
                    lista.append(str(0).zfill(2))
            
            matriz.append(lista)
            j += 1

            if len(matriz) == 5:
                  j = 0
                  imprimirMatriz(matriz)

def matriz(qtdColunas, qtdLinhas):
     
    matriz = []

    while len(matriz) <= qtdLinhas:

        lista = []

        for _ in range(qtdColunas):
                num = rd.randrange(10, 99)
                lista.append(num)

        matriz.append(lista)
    
    return matriz

def imprimirMatriz(matriz):
    
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()
     
print("\nMatriz: A")
criarMatrizes(aMatriz)

    

        
          



