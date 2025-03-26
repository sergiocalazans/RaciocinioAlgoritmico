# Exercício 1

'''
1. Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar.
'''

# Entrada

num = int(input("Digite um número inteiro: "))
resposta = ""

# Processamento

if num % 2 == 0:
    resposta = "Par"
else:
    resposta = "Ímpar"

# Saída

print(f"O número digitado é {resposta}.")