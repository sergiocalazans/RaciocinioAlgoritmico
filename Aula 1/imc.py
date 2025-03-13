# Definindo as variáveis de Entrada

nome = str(input('Qual o seu nome?'))
altura = float(input('Qual a sua altura? (em metros)' ))
peso = float(input('Qual o seu peso? (em Kg)'))

# Processamento

# Calculo do IMC
imc = peso / (altura ** 2)

# Saída

# Imprimi o resultado do IMC
print(f'{nome}, o seu IMC é: {imc}')
