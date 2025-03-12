# Definindo as variáveis de Entrada

nome = str(input('Qual o seu nome?'))
alturaNome = float(input('Qual a sua altura? (em metros)' ))
pesoNome = int(input('Qual o seu peso? (em Kg)'))

# Processamento

def calculoImc(altura, peso):

    imc = float(peso / (altura ** 2))
    resposta = ""

    if imc <= 18.5:
        resposta = "Abaixo do Peso"
    elif 18.5 <= imc < 25:
        resposta = "Peso Normal"
    elif imc in range(25, 30):
        resposta = "Sobrepeso"
    elif imc in range(30, 35):
        resposta = "Obesidade"
    else:
        resposta = "Imc não encontrado"

    return print(f'{nome}, o seu IMC é {int(imc)} e a classificação sua é {resposta}')
        

# Saída

calculoImc(alturaNome, pesoNome)