# Exercício 11

'''
11.	Construa um programa que sugira uma aposta de Mega-Sena ou seja, 
um algoritmo que gera e mostra um conjunto de 6 números aleatórios entre [1, 60] sem repetição. 
Em seguida, obtenha a aposta do usuário (sem repetição) e indique quantos acertos ele teve.
'''

from random import randint

# Entrada e Processamento
mega_aposta = []

while len(mega_aposta) < 6:
    num = randint(1, 60)
    if num not in mega_aposta:
        mega_aposta.append(num)

usuario_aposta = []
print("\nDigite sua aposta com 6 números entre 1 e 60 (sem repetir):\n")

while len(usuario_aposta) < 6:
    try:
        entrada = int(input(f"Número {len(usuario_aposta) + 1}: "))
        if entrada < 1 or entrada > 60:
            print("Número fora do intervalo. Tente novamente.")
        elif entrada in usuario_aposta:
            print("Número repetido. Tente outro.")
        else:
            usuario_aposta.append(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

acertos = 0

for valor in usuario_aposta:
    if valor in mega_aposta:
        acertos += 1

# Saída
print(f"\nAposta sorteada da Mega-Sena: {sorted(mega_aposta)}")
print(f"Sua aposta: {sorted(usuario_aposta)}")
print(f"Você acertou {acertos} número(s).\n")
