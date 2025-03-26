# Exercício 14

'''
14.	Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles. 
'''

# Entrada

# Solicita três números ao usuário e os armazena em uma lista
numeros = [int(input("Digite um número: ")) for _ in range(3)]

# Processamento

def maiorNumero(a, b, c):
    return max(a, b, c)

# Saída

print(f"\nO maior número é: {maiorNumero(*numeros)}.\n")
