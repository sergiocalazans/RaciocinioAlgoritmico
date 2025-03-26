# Exercício 11

'''
11. Elabore um algoritmo que, dada a idade de um nadador, 
mostre sua classificação segundo uma das seguintes categorias: 

•	5 até 7 anos: Infantil A; 
•	8 até 10 anos: Infantil B; 
•	11 até 13 anos: Juvenil A; 
•	14 até 17 anos: Juvenil B; 
•	Maiores de 18 anos: Adulto. 

'''

# Entrada

idade = int(input("Digite a idade do nadador: "))


# Processamento

def classificar_nadador(id): # id - idade

    if 5 <= id <= 7:
        return "Infantil A"
    elif 8 <= id <= 10:
        return "Infantil B"
    elif 11 <= id <= 13:
        return "Juvenil A"
    elif 14 <= id <= 17:
        return "Juvenil B"
    elif id >= 18:
        return "Adulto"
    else:
        return "Idade fora das categorias"

# Saída

print(f"Classificação: {classificar_nadador(idade)}")
