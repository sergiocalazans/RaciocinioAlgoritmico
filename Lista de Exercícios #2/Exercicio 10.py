# Exercicio 10

'''
10.	O IMC, índice de massa corporal, é calculado através da seguinte fórmula: 

IMC = massa / altura2 

Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário e 
mostre o valor do IMC e qual sua condição segundo o 
critério apresentado na tabela da OMS (Organização Mundial de Saúde): 

Condição                  IMC em adultos
    abaixo do peso           abaixo de 18,5
    no peso normal           entre 18,5 e 25
    acima do peso            entre 25 e 30
    Obeso                    acima de 30

'''

# Definindo as variáveis de Entrada

altura = float(input('\nQual a sua altura? (em metros) ' ))
peso = float(input('\nQual o seu peso? (em Kg) '))

# Processamento

# Função do cálculo do IMC
def calculoImc(h, p): # h - altura e p - peso

    imc = float(p / (h ** 2))
    resposta = ""

    if imc < 18.5:
        resposta = "Abaixo do Peso"
    elif imc < 25:
        resposta = "Peso Normal"
    elif imc < 30:
        resposta = "Sobrepeso"
    else:
        resposta = "Obesidade"
  
    # Retorna a impressão do resultado do IMC
    return print(f'O seu IMC é {round(imc, 2)} e a sua classificação é {resposta}.')
        

# Saída

# Chamando a função
calculoImc(altura, peso)