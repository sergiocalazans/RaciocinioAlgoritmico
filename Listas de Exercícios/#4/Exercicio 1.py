# Exercício 1

'''
1.	Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)
'''

from tabulate import tabulate # Biblioteca para criar tabelas no terminal

# Entrada e Processamentos

# Função para montar cada tabela
def tabela(i, x):

    tabela = [["Mutiplicação", "Resultado"]]

    for valor in x:

        tabela.append([f"{i}x{valor}", (i * valor)])

    print(f"\n\n{tabulate(tabela, headers="firstrow", tablefmt="fancy_grid")}")
    
# Função para imprimir cada tabela
def imprimir_tabelas():

    contador = 1
    intervalo = range(1, 11)

    while contador <= 10:

        tabela(contador, intervalo)
        contador += 1 

# Saída

imprimir_tabelas()
print("\nPrograma encerrou.")
