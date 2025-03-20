# Exercício 2

'''
2.	A partir do ano de nascimento informado pelo usuário, 
elabore um algoritmo que informe a idade que completará (ou já completou) em 2023. 
Verifique se ele já pode fazer a carteira de motorista ou não, informando sua situação.
'''

# Entrada

anoDigitado = int(input("Digite o seu ano de nascimento: "))
ano = 2023

# Processamento

idade = ano - anoDigitado
resposta = ""

if idade >= 18:
    resposta = "pode fazer a carteira de motorista."
else:
    resposta = "não pode fazer a carteira de motorista."

# Saída

print(f"Em {ano}, você {resposta}")