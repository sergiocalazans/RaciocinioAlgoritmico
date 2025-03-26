# Exercício 3

'''
3.	Elabore um algoritmo que leia um número inteiro e 
mostre sua raiz quadrada (informe “Valor inválido” para números negativos).
'''

# Importando a biblioteca Math

import math

# Entrada

while True:

    resposta = ""
    num = int(input("\nDigite um número inteiro: "))

    if num < 0:
        resposta = print("Valor inválido, digite um número inteiro")
        continue
    else:
        resposta = print("Valor válido.")
        break

# Processamento:

raizNum = round(math.sqrt(num), 2) # Cálculo da raíz quadrada

# Saída

print(f"A raíz quadrada do número é: {raizNum}.")