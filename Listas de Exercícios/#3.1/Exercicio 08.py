# Exercício 8

'''
8.	Faça um programa que gera uma lista dos números primos existentes 
entre 1 e um número inteiro informado pelo usuário.
'''

# ENTRADA
limite = int(input("Digite um número limite: "))
num_primos = []

# PROCESSAMENTO

for num in range(2, limite + 1):
    primo = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        num_primos.append(num)

# SAÍDA
print("Números primos:", num_primos)