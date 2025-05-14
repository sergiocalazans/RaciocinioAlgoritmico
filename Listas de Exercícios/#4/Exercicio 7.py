# Exercício 7

'''
7.	A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor máximo e o 
valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições inteiras e 
então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto fornecido.
'''

# Entrada

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Processamento e Saída

valor_min = min(vetor)
valor_max = max(vetor)

print(f"\nO valor mínimo do vetor é: {valor_min}")
print(f"O valor máximo do vetor é: {valor_max}")
print(f"A Amplitude Amostral do vetor é: {valor_max - valor_min}\n")
