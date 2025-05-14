# Exercício 8

'''
8.	Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número 
que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, 
mostre em qual(is) posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.
'''

# Entrada

i = 0
vetor = [1, 2, 3, 4, 5, 1, 7, 8, 9, 1]
num = int(input("\nQual número inteiro você quer pesquisar no vetor? "))
ocorrencias = 0

# Processamento e Saída

print()

for valor in vetor:

    if valor == num:
        ocorrencias += 1
        print(f"O número {valor} foi encontrado no vetor na posição {i}")
    
    i += 1

print(f"\nA quantidade de ocorrências foi de: {ocorrencias}.\n")
