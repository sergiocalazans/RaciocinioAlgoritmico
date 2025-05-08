# Exercício 2

'''
2.	Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
'''

from tabulate import tabulate # Biblioteca para criar tabelas no terminal

# Entrada

i = 1 # Contador i
x = 1 # Contador x
tabela = [["Mutiplicação", "Resultado"]] # Lista que monta a tabela
qtd = 10 # Quantidade de tabelas

# Processamento

while i <= qtd:

    tabela.append([f"{i}x{x}", (i * x)])

    if tabela[-1][1] == i * 10:
        
        x = 0
        i += 1
        tabela.append(["", ""])
    
    x += 1

# Saída
tabela.pop(-1) # Exclui a última linha em branco da tabela
print(f"\n\n{tabulate(tabela, headers="firstrow", tablefmt="fancy_grid")}") # Imprimi a tabela
print("\nPrograma encerrou.")