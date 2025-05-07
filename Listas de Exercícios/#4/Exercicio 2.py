# Exercício 2

'''
2.	Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
'''

from tabulate import tabulate # Biblioteca para criar tabelas no terminal

# Entrada

tabela = [["Mutiplicação", "Resultado"]]
contador = 1

# Processamento

def calcular_tabela(tabela, contador):

    while contador <= 10:

        tabela.append([f"1x{contador}", (1 * contador)])
        contador += 1

    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))

# Saída

calcular_tabela(tabela, contador)