# Exercício 6

'''
6.	Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 - feminino) 
elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as seguintes fórmulas:

    a.	para homens: p = (72.7 * h) - 58
    b.	para mulheres: p = (62.1 * h) - 44.7

'''

# Entrada 

altura = float(input("\nDigite a altura: "))


while True:

    sexo = int(input("\nDigite o sexo da pessoa:  (use 1 - masculino e 2 - feminino) "))

    if sexo in [1, 2]:
        print("\nValor válido.")
        break
    else:
        print("\nValor inválido.")

# Processamento

def calculoPesoIdeal(h):

    if sexo == 1:
        peso = (72.7 * h) - 58
    else: 
        peso = (62.1 * h) - 44.7
    
    return print(f"\nO peso ideal deve ser: {round(peso, 2)} Kg.\n")

# Saída

calculoPesoIdeal(altura)
    