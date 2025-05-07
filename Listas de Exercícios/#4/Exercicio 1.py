# Exercício 1

'''
1.	Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)
'''

from tabulate import tabulate # Biblioteca para criar tabelas no terminal

# Entrada

tabela = [["Mutiplicação", "Resultado"]]

# Processamento

def calcular_tabela(tabela):

    for valor in range(1, 11):

        tabela.append([f"1x{valor}", (1 * valor)])

    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))

# Saída

calcular_tabela(tabela)



