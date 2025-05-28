# Exercício 5

'''
5.	Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do intervalo 10 a 99. 
Modifique então a matriz de forma que, caminhando da esquerda para a direita, 
de cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. 
Mostre a matriz antes e depois da modificação.
'''

from random import randint

def gerar_matriz_15x7():
    return [[randint(10, 99) for _ in range(7)] for _ in range(15)]

def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:3}" for elem in linha))
    print()

def reorganizar_matriz_par_impar(matriz):
    # Flatten da matriz original
    elementos = [num for linha in matriz for num in linha]
    
    # Separar pares e ímpares
    pares = [num for num in elementos if num % 2 == 0]
    impares = [num for num in elementos if num % 2 != 0]
    
    reorganizados = pares + impares
    
    # Recriar a matriz com os elementos reorganizados
    nova_matriz = []
    for i in range(15):
        linha = reorganizados[i*7:(i+1)*7]
        nova_matriz.append(linha)
    
    return nova_matriz

matriz_original = gerar_matriz_15x7()

print("Matriz original:")
exibir_matriz(matriz_original)

matriz_modificada = reorganizar_matriz_par_impar(matriz_original)

print("Matriz com pares primeiro e ímpares depois:")
exibir_matriz(matriz_modificada)
