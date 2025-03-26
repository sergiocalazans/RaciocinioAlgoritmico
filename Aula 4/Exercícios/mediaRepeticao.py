# Exercício 2

'''
2) Implemente um programa em Python para ler
do teclado números. Caso o usuário forneça
um numero igual a -1, o programa deve fornecer
a média dos números e encerrar

10  60  20
soma = 90
media = soma / qtde de numeros
'''

soma = 0
contador = 0
entrada = 0
while entrada != -1:
    entrada = float(input('Entre com o número: '))
    if entrada != -1:
        soma = soma + entrada
        contador += 1 # contador = contador + 1

print('A media é: ', soma / contador)

