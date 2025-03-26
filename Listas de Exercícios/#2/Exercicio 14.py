# Exercício 14

'''
14.	Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles. 
'''

# Entrada

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))
num3 = int(input("\nDigite o terceiro número: "))

# Processamento

def maiorNumero(a, b, c):
    return max(a, b, c)

# Saída

print(f"\nO maior número é: {maiorNumero(num1, num2, num3)}.\n")
