# Exercício 5

'''
5.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# ENTRADA
num = int(input("\nDigite um número inteiro para calcular o fatorial: "))
resultado = 1

# PROCESSAMENTO
for i in range(1, num + 1):
    resultado *= i

# SAÍDA
print(f"{num}! = {resultado}\n")