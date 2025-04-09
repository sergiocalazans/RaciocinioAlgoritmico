# Exercício 11

'''
11.	Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
'''

# ENTRADA
n = int(input("\nDigite um valor para N: "))

# PROCESSAMENTO
def calcular_h(n):
    h = sum(1 / i for i in range(1, n + 1))
    return round(h, 3)

# SAÍDA
print(f"\nValor de H: {calcular_h(n)}\n")