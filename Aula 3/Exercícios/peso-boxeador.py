# Exercício 3

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