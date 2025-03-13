# Definindo as variáveis de Entrada

nome = str(input('Qual o seu nome?')).strip()
alturaNome = float(input('Qual a sua altura? (em metros)' ))
pesoNome = int(input('Qual o seu peso? (em Kg)'))

# Processamento

# Função para calcular o IMC
def calculoImc(altura, peso):

    imc = float(peso / (altura ** 2))
    resposta = ""

    if imc <= 18.5:
        resposta = "Abaixo do Peso"
    elif 18.5 <= imc < 25:
        resposta = "Peso Normal"
    elif 25 <= imc < 30:
        resposta = "Sobrepeso"
    elif 30 <= imc < 35:
        resposta = "Obesidade"
    else:
        resposta = "não encontrado"


    # Retorna a impressão do resultado do IMC
    return print(f'{nome}, o seu IMC é {int(imc)} e a sua classificação é {resposta}')
        

# Saída

# Chamando a função
calculoImc(alturaNome, pesoNome)