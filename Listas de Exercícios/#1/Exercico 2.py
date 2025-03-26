# Resolução Exercício 2

''' 2. Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade que completará em 2022.'''

# Definindo variáveis de Entrada

anoDigitado = int(input("Digite o ano de nascimento:")) 
ano = 2022


# Processamento

idade = ano - anoDigitado

# Saída

print(f"Em {ano}, você fez {idade} anos.")