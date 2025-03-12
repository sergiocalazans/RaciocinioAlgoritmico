# Definindo as variáveis de Entrada

nome = str(input('Qual o seu nome?'))
altura = float(input('Qual a sua altura? (em metros)' ))
peso = int(input('Qual o seu peso? (em Kg)'))

# Processamento

imc = peso / (altura ** 2)

# Saída

print(f'{nome}, o seu IMC é: {imc}')