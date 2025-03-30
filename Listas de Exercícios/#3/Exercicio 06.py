# Exercício 6

'''
6.	Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de 1 a 20 polegadas. 
A conversão entre estas duas unidades é dada por: 

polegada = centímetro x 2,54

'''

# Importando a biblioteca tabulate

from tabulate import tabulate

# Entrada

contadorPolegadas = 1
tabelaConversao = [
    ["Polegadas", "Centímetros (cm)"]
]

# Processamento

while contadorPolegadas <= 20:

    cm = round((contadorPolegadas / 2.54), 2)
    tabelaConversao += [[contadorPolegadas, cm]]

    contadorPolegadas += 1

# Saída 

print(tabulate(tabelaConversao, headers= 'firstrow', tablefmt='fancy_grid'))