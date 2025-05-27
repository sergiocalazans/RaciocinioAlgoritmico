# Exercício 2

'''
2.	Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros fornecida pelo usuário 
por um número também fornecido pelo usuário.

Lembrete: para multiplicar uma matriz Am×n por um escalar k, 
basta multiplicar cada entrada aij de A por k. 
Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij.  

'''

def ler_matriz_3x3():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplicar_matriz_por_escalar(matriz, escalar):
    return [[escalar * elemento for elemento in linha] for linha in matriz]

def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:5}" for elem in linha))

matriz = ler_matriz_3x3()
escalar = int(input("Digite o número para multiplicar a matriz: "))

resultado = multiplicar_matriz_por_escalar(matriz, escalar)

print("\nMatriz original:")
exibir_matriz(matriz)

print(f"\nMatriz resultante após multiplicação por {escalar}:")
exibir_matriz(resultado)
