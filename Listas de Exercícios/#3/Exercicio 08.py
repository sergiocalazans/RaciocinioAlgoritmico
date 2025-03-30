# Exercício 8

'''
8.	Elabore um algoritmo que leia um conjunto de 10 números inteiros. 
Mostre então qual o valor da soma e da média aritmética do conjunto.

'''

# Entrada

# Solicita dez números ao usuário e os armazena em uma lista
numeros = [int(input("Digite um número: ")) for _ in range(10)]

# Processamento

def somaMedia(conjunto):

    soma = sum(conjunto)
    media = soma / len(conjunto)
    
    return print(f"\nA soma do conjunto é {soma} e a média aritmética é {media}.\n")

# Saída

somaMedia(numeros)