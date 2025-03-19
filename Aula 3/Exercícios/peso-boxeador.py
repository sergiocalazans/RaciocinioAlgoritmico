# Exercício 3

'''
Escreva um algoritmo que dado o peso de um boxeador, informe
a categoria a qual ele pertence, seguindo a tabela abaixo:
Categoria       Peso (Kg)
 Palha            Menor que 50 Kg
 Pluma            50 - 59,99
 Leve             60 - 75,99
 Pesado           76 - 87,99
 Super Pesado     Maior que 88 Kg
'''

# Entrada

pesoDigitado = float(input("Digite o peso: (em Kg, formato: xx.xx) "))

# Processamento

def calculoCategoria(peso):

    resposta = ""

    if peso < 50:
        resposta = "Palha"
    elif peso < 60:
        resposta = "Pluma"
    elif peso < 76:
        resposta = "Leve"
    elif peso < 88:
        resposta = "Pesado"
    elif peso >= 88:
        resposta = "Super Pesado"
    else:
        resposta = "não encontrado"

    return print(f"Sua categoria é: {resposta}")

# Saída

calculoCategoria(pesoDigitado)