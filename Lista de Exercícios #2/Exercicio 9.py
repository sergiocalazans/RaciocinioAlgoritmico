# Exercício 9

'''
9.	A partir da idade informada de uma pessoa, 
elabore um algoritmo que informe a sua classe eleitoral, 
sabendo que menores de 16 não votam (não votante), 
que o voto é obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e 
que o voto é opcional para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo). 
'''

# Entrada 

idade = int(input("\nDigite sua idade: "))

# Processamento

# Função de classificação eleitoral
def classeEleitoral(id): # id - idade

    resposta = ""

    if id < 16:
        resposta = "não votante"

    elif 16 >= id <= 18 or id > 65:
        resposta = "eleitor facultativo"
    
    else:
        resposta = "eleitor obrigatório"

    # Retorna a classificação eleitoral
    return print(f"\nA sua classe eleitoral é {resposta}.\n")

# Saída

# Chamando a função
classeEleitoral(idade)