# Exercício 3

'''
Escreva um algoritmo que dado o peso de um boxeador,
informe a categoria a qual ele pertence, seguindo
a tabela abaixo:

Categoria				Peso (Kg)
Palha					Menor que 50 Kg
Pluma					50 - 59,99
Leve					60 - 75,99
Pesado					7 - 87,99
Super Pesado			Maior que 88 Kg
'''

while True:
    # peso >= 0 e peso <= 150
    peso = -1

    while peso < 0 or peso > 150:
        peso = float(input('Entre com o peso do boxeador: '))

    if peso < 50:
        categoria = 'palha'
    elif peso < 60:
        categoria = 'pluma'
    elif peso < 76:
        categoria = 'leve'
    elif peso < 88:
        categoria = 'pesado'
    else:
        categoria = 'super pesado'

    print('A categoria é: ', categoria)

    opcao = input('Deseja continuar (s/n): ')
    if opcao != 's':
        break

print('obrigado por usar este programa!')