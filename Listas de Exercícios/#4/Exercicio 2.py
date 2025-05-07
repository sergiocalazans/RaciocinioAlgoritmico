# Exercício 2

'''
2.	Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
'''

from tabulate import tabulate # Biblioteca para criar tabelas no terminal

# Entrada

i = 1
contador = 1
tabela = [["Mutiplicação", "Resultado"]]

# Processamento

while i <= 10:

    tabela.append([f"{i}x{contador}", (i * contador)])

    if tabela[-1][1] == i * 10:
        
        contador = 0
        i += 1
        tabela.append(["", ""])
    
    contador += 1

# Saída
tabela.pop(-1)
print(f"\n\n{tabulate(tabela, headers="firstrow", tablefmt="fancy_grid")}") 
print("\nPrograma encerrou.")