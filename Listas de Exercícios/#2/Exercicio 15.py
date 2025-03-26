# Exercício 15

'''
15.	Escreva um algoritmo que leia três números inteiros e mostre-os em ordem decrescente. 
'''

# Entrada

# Solicita três números ao usuário e os armazena em uma lista
numeros = [int(input("Digite um número: ")) for _ in range(3)]

# Processamento

def ordenarDecrescente(a, b, c):
    # Retorna a lista de números ordenada em ordem decrescente
    return sorted([a, b, c], reverse=True)

# Saída

print(f"\nNúmeros em ordem decrescente: {ordenarDecrescente(*numeros)}.\n")
