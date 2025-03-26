# Exercício 7

'''
7.	O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula: 

IMC = massa / altura²

Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário e 
mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o 
critério apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. 
Caso não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9).

'''

# Entrada

altura = float(input('\nQual a sua altura? (em metros) '))
peso = float(input('\nQual o seu peso? (em Kg) '))

# Processamento

def calculoImc(h, p):

    imc = round(float(p / (h ** 2)), 2)
    resposta = ""

    if 18.5 <= imc < 25:
        resposta = f"o seu IMC é normal."
    else:
        p = round(float(24.9 * (h ** 2)), 2)
        resposta = f"o seu IMC não está normal e sua massa considerada normal seria {p} Kg."

    return print(f"\nResultado: {resposta}\n")
        

# Saída

calculoImc(altura, peso)
