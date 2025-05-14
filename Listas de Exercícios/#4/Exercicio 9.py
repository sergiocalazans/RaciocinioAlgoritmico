# Exercício 9

'''
9.	Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido. 
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, 
e vImpares contendo somente os números ímpares de vLido. 
Os vetores vPares e vLido não deverão conter zeros. Mostre então os três vetores.
'''

# Entrada
print()
i = 1
num = 0
vLido = []
vPares = []
vImpares = []

while i <= 10:

    while num == 0:
        num = int(input("Digite um número inteiro (exceto zero): "))

    vLido.append(num)
    i += 1
    num = 0

# Processamento

for valor in vLido:

    if valor % 2 == 0:
        vPares.append(valor)
    else:
        vImpares.append(valor)

# Saída

print(f"\nO vetor dos números digitados:\n {vLido}")
print(f"\nO vetor dos números pares:\n {vPares}")
print(f"\nO vetor dos números ímpares:\n {vImpares}")
