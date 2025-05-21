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

def criarMatriz(nMatriz): 

    j = 1
    i = 0
    matriz_original = matriz(5, 5)

    while len(nMatriz) <= 5:

        for linha in matriz_original:
                
                lista = []

                for elemento in linha:

                    if elemento == linha[2]:
                        lista.append(str(elemento))
                    else:
                        lista.append(str(0).zfill(2))
                    
                nMatriz.append(lista)
                j += 1

    imprimirMatriz(nMatriz)

def matriz(qtdColunas, qtdLinhas):
     
    matriz = []
    i = 0

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
criarMatriz(aMatriz)

    

        
          



