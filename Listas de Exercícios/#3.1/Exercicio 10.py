# Exercício 10

'''
10.	Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
No final, mostre a soma também.
'''

# ENTRADA
n = int(input("\nDigite o número de termos da série: "))
soma = 0

# PROCESSAMENTO
for i in range(1, n + 1):
    soma += i / (2 * i - 1)

# SAÍDA
print(f"\nSoma da série: {round(soma, 3)}\n")