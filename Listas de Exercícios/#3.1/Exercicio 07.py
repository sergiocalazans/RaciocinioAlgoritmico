# Exercício 7

'''
7.	Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

# ENTRADA
num = int(input("\nDigite um número inteiro: "))

# PROCESSAMENTO
def num_primo(n):
    if n < 2:
        return "Não"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Não"
    return "Sim"

# SAÍDA
print(f"\n{num} é primo? {num_primo(num)}\n")