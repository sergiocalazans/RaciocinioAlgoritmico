# Exercício 3

'''
3.	Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, 
sorteados dentro do intervalo 100 a 999, garantindo que não haverá nenhuma repetição 
(os 16 números devem ser únicos). Encontre então o valor do menor elemento da linha em que 
se encontra o maior elemento da matriz. Mostre a matriz e os dois valores encontrados.
'''

from random import sample

def gerar_matriz_4x4_unica():
    numeros = sample(range(100, 1000), 16)  # 16 números únicos entre 100 e 999
    matriz = [numeros[i*4:(i+1)*4] for i in range(4)]  # Converte em matriz 4x4
    return matriz

def encontrar_maior_elemento(matriz):
    maior = matriz[0][0]
    linha_maior = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                linha_maior = i
    return maior, linha_maior

def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:4}" for elem in linha))

matriz = gerar_matriz_4x4_unica()
maior, linha_maior = encontrar_maior_elemento(matriz)
menor_na_linha = min(matriz[linha_maior])

print("Matriz 4x4 gerada:")
exibir_matriz(matriz)

print(f"\nMaior elemento da matriz: {maior}")
print(f"Menor elemento na linha do maior: {menor_na_linha}")
