# Exercício 7

'''
7.	Considerando que 1 milha vale exatamente 1.609,344 metros, 
imprima uma tabela de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10 quilômetros.

'''

# Importando a biblioteca tabulate 
from tabulate import tabulate  

# Entrada 
milha_metros = 1609.344

dados = []  # Lista para armazenar os valores convertidos

# Processamento

# Loop para converter de 20 km a 160 km em passos de 10 km
for km in range(20, 161, 10):
    metros = km * 1000  # Converte quilômetros para metros
    milhas = metros / milha_metros  # Converte metros para milhas
    dados.append([km, milhas])  # Adiciona os valores à lista


# Saída
print(tabulate(dados, headers=["Km", "Milhas"], tablefmt="fancy_grid"))
