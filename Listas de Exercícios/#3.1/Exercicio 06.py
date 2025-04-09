# Exercício 6

'''
6.	Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar 
se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, 
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

# ENTRADA

idades = []

while True:
        idade = int(input("Digite a idade (ou -1 para sair): "))
        if idade == -1:
            break
        idades.append(idade)

# PROCESSAMENTO

def classificar_turma(lista):

    media = sum(lista) / len(lista)

    if media <= 25:
        print("Turma Jovem")
    elif media <= 60:
        print("Turma Adulta")
    else:
        print("Turma Idosa")

# SAÍDA
classificar_turma(idades)